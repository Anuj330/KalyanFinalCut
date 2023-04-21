from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import userdetails, Payment
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from .forms import PaymentdetailsForm, userdettailsForm
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum

# Create your views here.

def Home(request):
    return render(request, "home.html")

def About(request):
    a = datetime(2022, 4, 1)
    b = datetime.now()
    b.strftime('%Y-%m-%d')
    c = b-a
    print(f"days: {c.days}")
    context = {"c": c}
    return render(request, "about.html", context)

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
    for i in room_messages:
        membership_no = i.Membership_number
        print(membership_no)
    # return membership_no
    context = {"user" : user , "rooms" : rooms, 'room_messages' : room_messages}
    return render(request,'memberPage.html' , context)

def MemberForm(request):
    form  = PaymentdetailsForm()
    
    date = datetime.now()
    print(date)
    print(request.user)
    context = {'form': form, 'date': date}
    if request.method == "POST":
        host = request.user
        Name = request.POST.get('Name', '')
        Phone = request.POST.get('Phone', '')
        Ac_No = request.POST.get('Ac_No', '')
        Month = request.POST.get('Month', '') 
        Share_Money = request.POST.get('Share_Money', '')
        Late_Charge = request.POST.get('Late_Charge', '')
        Balance = request.POST.get('Balance', '')
        Payments = Payment(host = host, Name=Name, Phone=Phone, Ac_No=Ac_No, Month=Month, Share_Money=Share_Money, Late_Charge=Late_Charge, Balance=Balance)
        payment_id = Payments.id 
        if payment_id == None:
            random_id = random.randint(1, 10000000000000)
            payment_id = random_id
        print(payment_id)
        Payments.save()
        param_dict={

            'MID': 'nzUJdA10034995022680',
            'ORDER_ID': str(payment_id),
            'TXN_AMOUNT': str(Share_Money),
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }
        return  render(request, 'paytm.html', {'param_dict': param_dict})
    # return redirect('memberPage')
    return render(request, "memberForm.html", context)

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    # form = request.POST
    # response_dict = {}
    # for i in form.keys():
    #     response_dict[i] = form[i]
    #     if i == 'CHECKSUMHASH':
    #         checksum = form[i]

    # verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    # if verify:
    #     if response_dict['RESPCODE'] == '01':
    #         print('order successful')
    #     else:
    #         print('order was not successful because' + response_dict['RESPMSG'])
    # return render(request, 'paymentstatus.html', {'response': response_dict})
    return HttpResponse("done")

def editDetails(request):
    forms = userdettailsForm()
    print(userdettailsForm())
    if request.method == 'POST':
        Name = request.user
    return render(request, 'edit_user_details.html')

def adminPage(request):
    users = User.objects.all()
    print(users)
    room_messages = userdetails.objects.all()
    # for i in room_messages:
    #     print(i.Name)
    # Payments = Payment.objects.all()
    # for i in Payments:
    #     print(i)
    context = {'room_messages' : room_messages }
    return render(request,'Admin.html', context ) 

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


