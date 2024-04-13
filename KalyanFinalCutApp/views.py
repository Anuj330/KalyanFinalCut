from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import userdetails, Payment
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from .forms import PaymentdetailsForm, userdettailsForm
from django.http import HttpResponse, JsonResponse
import random
from django.views.decorators.csrf import csrf_exempt
# from paytm import Checksum
from . import keys

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
    page = 'login'
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
        else:
            messages.error(request, "username or password wrong!!!")  

    context = {'page' : page}      
    return render(request, 'login.html', context)

def Adminlogin(request):
    page = 'Adminlogin'
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
            return redirect('adminPage')
        else:
            messages.error(request, "username or password wrong!!!")  

    context = {'page' : page}      
    return render(request, 'login.html', context)

def contact(request):
    return render(request, 'contact.html')


def MemberPage(request):
    user = User.objects.get(username__iexact=request.user)
    rooms = user.payment_set.all()
    room_messages = user.userdetails_set.all()
    for i in room_messages:
        membership_no = i.Membership_number
        print(membership_no)
    context = {"user" : user , "rooms" : rooms, 'room_messages' : room_messages}
    return render(request,'memberPage.html' , context)
#
import datetime
#

global balance

def MemberForm(request):
    balance = 0
    form = PaymentdetailsForm(request.POST or None)

    date = datetime.datetime.now()
    print(date)
    print(request.user)
    users = User.objects.all()
    if request.method == "POST":
        host_id = request.POST['host_id']
        try:
            host = User.objects.get(id=host_id)  # Fetch the selected host user

        except User.DoesNotExist:
            return redirect('invalid_host')
        Month = request.POST.get('Month','')
        # Start_date = datetime.datetime.strptime(request.POST.get('Start_date', '1111-11-11'), '%Y-%m-%d')
        Start_date = request.POST.get('Start_date','1111-11-11')
        # Finish_date = datetime.datetime.strptime(request.POST.get('Finish_date', '1111-11-11'), '%Y-%m-%d')
        Finish_date = request.POST.get('Finish_date','1111-11-11')
        Share_Money = request.POST.get('Share_Money', '')
        Late_Charge = request.POST.get('Late_Charge', '')
        rooms = host.payment_set.all()
        current_date = Start_date
        if Start_date not in ['1111-11-11', '']:
            Start_date = datetime.datetime.strptime(Start_date, '%Y-%m-%d')
            current_date = Start_date
            Finish_date = datetime.datetime.strptime(Finish_date, '%Y-%m-%d')
            for i in rooms:
                balance += i.Share_Money
            while current_date <= Finish_date:
                # Move to the next month
                current_date = current_date.replace(day=15)
                if current_date <= Finish_date:  # Ensure we haven't exceeded the finish date
                    print("Inside the loop")
                    balance += int(Share_Money)
                    Balance = balance
                    Payments = Payment.objects.create(host=host, Month=current_date, Share_Money=Share_Money,
                                                      Late_Charge=Late_Charge, Balance=Balance)
                    payment_id = Payments.id
                    if payment_id is None:
                        random_id = random.randint(1, 10000000000000)
                        payment_id = random_id
                    print(payment_id)
                    Payments.save()
                    Late_Charge_balance = 0
                    for i in rooms:
                        Late_Charge_balance += i.Late_Charge
                    print(f'late charge is {Late_Charge_balance}')

                # Move to the next month after processing
                current_date += relativedelta(months=1)

        else:
            for i in rooms:
                balance += i.Share_Money
            Balance = balance
            Payments = Payment.objects.create(host=host, Month=Month, Share_Money=Share_Money, Late_Charge=Late_Charge,
                                              Balance=Balance)
            payment_id = Payments.id
            if payment_id == None:
                random_id = random.randint(1, 10000000000000)
                payment_id = random_id
            print(payment_id)
            Payments.save()
            Late_Charge_balance = 0
            for i in rooms:
                Late_Charge_balance += i.Late_Charge
            print(f'late charge is {Late_Charge_balance}')

    context = {'users' : users, 'form': form, 'date': date}
    return render(request, "memberForm.html", context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def get_user_details(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'GET':
        user_id = request.GET.get('user_id')
        user_details = get_object_or_404(userdetails, user_id=user_id)

        data = {
            'Name': user_details.Name,
            'phone_number': user_details.phone_number,
            # 'balance': user_details.balance,
            # Add more fields here
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def moreDetails(request, id):
    # user = User.objects.get(id = id)
    # room_messages = user.userdetails_set.all()
    room_messages = get_object_or_404(userdetails, id = id)
    context = {'room_messages' : room_messages}

    return render(request,'moreDetails.html', context)

def editDetails(request):
    form = userdettailsForm()
    print(userdettailsForm())
    context = {'form': form}
    if request.method == 'POST':
        user = request.user
        user = form.save(commit=False)
        user.save()
            
        return redirect("memberPage")
    else:
        messages.error(request, "something went wrong")
    
    return render(request,'edit_user_details.html', context)

# @login_required(login_url= 'Adminlogin')
def adminPage(request):
    users = User.objects.all()
    print(users)
    room_messages = userdetails.objects.all()
    context = {'room_messages' : room_messages }
    return render(request,'Admin.html', context ) 

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #this will save the user in a flash so u will be able to use it right away
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            user.save()
            messages.success(request, "sucess!!!")
            login(request, user)
        else:
            messages.error(request, "something went wrong")
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request,'reg2.html', context)    

def anujpage(request):
    return render(request, "anuj.html")

def location(request):
    rooms = userdetails.objects.all()
    context = {'rooms' : rooms}
    return render(request, "location.html", context)


def pay(request):
    print("helllo")
    return render(request, 'payment.html') 

def refer(request):
    rooms = userdetails.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'table.html', context)

# def sendMessage(request):
#     # pass
#     client = Client(keys.Acoount_SID, keys.Auth_key)
#
#     message = client.messages.create(
#         from_= keys.twilio_nunmber,
#         to=keys.my_phone_number,
#         body="Dear Member, your latest txn corresponding this account 3,004,887,558 is Txn:200.0,fine:0.0,bal:1400.0 .TEAM LAXMI"
#         )
#
#     print(message.body)
