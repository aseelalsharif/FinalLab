from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Product
from .models import Order
from .models import OrderItem
from .models import Shipping




    


 
    
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)