from itertools import product
from ntpath import join
from pickle import FALSE
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import datetime 

from .models import *



# Create your views here.
def Products(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, creared = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
       items = [] # make you seee the cart when you logout the admin
       order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
       cartItems= order['get_cart_items']
        
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)
    

def cart(request):
    order = None
    items = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, creared = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        # make you see the cart when you logout the admin
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
    context = {'items': items, 'order': order}
    return render(request, 'products/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, creared = Order.objects.get_or_create(
         customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = [] # make you seee the cart when you logout the admin
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False }
        cartItems= order['get_cart_items']

    context = {'items': items, 'order': order}
    return render(request, 'products/checkout.html', context)

# click


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)

    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        customer = Customer.objects.create(
            user = request.user,
            name = request.user.username,
            email = request.user.email
        )

    product = Product.objects.get(id=productId)
    order, creared = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, creared = OrderItem.objects.get_or_create(
        order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer=request.user.customer
        order, creared = Order.objects.get_or_create(
        customer = customer, complete=False)
        total= float (data['form']['total'])
        order.transaction_id = transaction_id 
        
        if total == float(order.get_cart_total): #make sure the total sent the same total incart total
          order.complete =True
        order.save()
        
        if order.shipping ==True:  
            Shipping.objects.create(
             customer=customer,
              order=order,
              address= data['shipping']['address'],
              city= data['shipping']['city'],
              state= data['shipping']['state'],
              zipcode= data['shipping']['zipcode'],
              
            )
        
    else:    
        print ('The user is not login') 
    return JsonResponse('Payment complete', safe=False)

