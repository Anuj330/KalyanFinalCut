from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = "home"),
    path('about/', views.About, name = "about"),
    path('causes/', views.causes, name= "causes"),
    path('portfolio/', views.portfolio, name= 'portfolio'),
    path('login/', views.loginPage, name= 'login'),
    path('Adminlogin/', views.Adminlogin, name= 'Adminlogin'),
    path('anuj/', views.anujpage, name = 'anuj'),
    path("location/", views.location, name = "location"),
    path('moreDetails/<int:id>/', views.moreDetails, name = "moreDetails"),
    path('contact/', views.contact, name = 'contact' ),
    path('memberPage/', views.MemberPage, name = "memberPage"),
    path('memberForm/', views.MemberForm, name = "memberForm"),
    path('editDetails/', views.editDetails, name = "editUser"),
    path("logout/", views.logoutUser, name = "logout"),
    path('register/', views.registerPage, name = 'register'),   
    path('adminPage/', views.adminPage, name = "adminPage"),  #can be used for style with table
    # path("handlerequest/", views.handlerequest, name="handleRequest"),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    # path('#/', views.sendMessage, name = "msg"),
    path("pay/", views.pay, name="pay"),
    path("table/", views.refer, name="table"),

]
