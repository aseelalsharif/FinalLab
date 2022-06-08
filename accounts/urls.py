from . import views
from django.urls import path
from django.contrib.auth import views as auth_view # login and logout
urlpatterns = [
    path('Sign Up/', views.SignUp, name='Sign Up'), 
    path('profile/', views.Profile, name='profile'),
    path('Login/', auth_view.LoginView.as_view(template_name='register/Login.html'), name='Login'),
     path('logout/', auth_view.LogoutView.as_view(template_name='register/LogOut.html'), name='logout'),
]