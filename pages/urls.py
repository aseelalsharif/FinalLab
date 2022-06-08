from . import views
from django.urls import  path

urlpatterns = [
    path('contactUs',views.contactUs, name='contactUs'),
    path('', views.home, name='Home'),
    path('About',views.About, name='About'),
]