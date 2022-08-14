from django.urls import path
from .views import *

urlpatterns = [
    path('',  index, name='index'),
    path('apply',  apply, name='apply'),
    path('contact',  contact, name='contact'),
    path('detail',  detail, name='detail'),
    path('dashboard', dashboard, name='dashboard'),
    path('about',  about, name='about'),
    path('login',  loginuser, name='login'),
    path('register',  register, name='register'),
    path('logout', logoutuser , name='logout'),
]