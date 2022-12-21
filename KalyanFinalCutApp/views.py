from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import userdetails, Payment
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Home(request):
    return render(request, "home.html")

def About(request):
    return render(request, "about.html")

def causes(request):
    return render(request, 'loan.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'user not found')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('memberPage')        
    return render(request, 'login.html' )

def contact(request):
    return render(request, 'contact.html')


def MemberPage(request):
    user = User.objects.get(username__iexact=request.user)
    rooms = user.payment_set.all()
    room_messages = user.userdetails_set.all()
    # topics = Topic.objects.all()
    context = {"user" : user , "rooms" : rooms, 'room_messages' : room_messages}
    return render(request,'memberPage.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #this will save the user in a flash so u will be able to user it right away
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "something went wrong")
    
    context = {'form': form}
    return render(request,'registration.html', context)
