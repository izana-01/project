from django.contrib import admin
from django.urls import path,include
from finalapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('otpverify/',views.otpverify,name='otpverify'),
    
]