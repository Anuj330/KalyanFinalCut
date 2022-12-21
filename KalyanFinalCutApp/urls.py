from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = "home"),
    path('about/', views.About, name = "about"),
    path('causes/', views.causes, name= "causes"),
    path('portfolio/', views.portfolio, name= 'portfolio'),
    path('login/', views.loginPage, name= 'login'),
    path('contact/', views.contact, name = 'contact' ),
    path('memberPage/', views.MemberPage, name = "memberPage"),
    path("logout/", views.logoutUser, name = "logout"),
    path('register/', views.registerPage, name = 'register')
]
