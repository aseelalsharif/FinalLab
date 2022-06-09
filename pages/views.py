from django.shortcuts import render
from . models import Contact
from . models import Home
# Create your views here.



def contactUs(request):
    if request.method == 'POST':
        v_name= request.POST.get('firstname')
        v_email = request.POST.get('email')
        v_subject = request.POST.get('subject')
        v_massage = request.POST.get('massage')
        v_contact = Contact(name=v_name, email=v_email, subject=v_subject, massage=v_massage)
        v_contact.save()
        return render(request, 'Pages/ThankYou.html')
    else:
        return render(request,'Pages/Contact.html')

def home(request):
    Content = Home.objects.all().first()

    return render(request,'Pages/Home.html', {'Content': Content})

def About(request):
    return render(request,'Pages/About.html')