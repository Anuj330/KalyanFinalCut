from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .choices import GENDER_TYPE_CHOICE
import django
from django.core.exceptions import ObjectDoesNotExist


# def get_expiry():
#     return datetime.today() + timedelta(days=30)

# User = get_user_model()
class Payment(models.Model):    
    host = models.ForeignKey(User, on_delete = models.CASCADE, null=True )
    Name = models.CharField(max_length=400, null= True,blank=True)
    # share_money = models.IntegerField(null = True , blank=True)
    Ac_No = models.IntegerField(null = True , blank=True, default= 0)
    Phone = models.IntegerField(null = True , blank=True, default= 0)
    Month = models.DateField(null = True, blank=True)
    Share_Money = models.IntegerField(null = True , blank=True, default=0)
    Late_Charge = models.IntegerField(null = True , blank=True, default=0)
    Balance = models.IntegerField(null = True , blank=True, default= 0)
    # Date = models.DateField(null = True, blank=True)

     
    def __str__(self):
        return str(self.host) +'['+str(self.Month)+']' + '['+str(self.Name)+']'


class loan(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=400, null= True,blank=True)
    Ac_No = models.IntegerField(null = True , blank=True, default= 0)
    loan_date = models.DateField(null = True, blank=True)
    loan_amount = models.FloatField(null=True,blank=True,default=0)
    loan_intrest_rate = models.FloatField(null=True,blank=True,default=0) 
    loan_principle = models.FloatField(null=True, blank=True, default=0)
    loan_intrest_amount = models.FloatField(null=True, blank=True, default=0)

    def __str__(self) -> str:
        return "["+str(self.loan_date)+']' + '['+str(self.name)+']' + '['+str(self.Ac_No)+']'
    

# def get_expiry():
#     return datetime.today() + timedelta(days=30)  

class location(models.Model):
    locations = models.CharField(max_length=400, null= True,blank=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return str(self.locations)

class userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # first_pay = models.ForeignKey(Payment, on_delete=models.CASCADE) #SET_NULL to save the messages of the room\
    Name = models.CharField(max_length=100, null=True, blank=True,)
    Date_of_birth = models.DateField(null = True, blank=True)
    gender = models.PositiveBigIntegerField(choices=GENDER_TYPE_CHOICE)
    Membership_number = models.IntegerField(null=True, blank=True)
    Date_of_joining = models.DateField(null = True, blank=True)
    Address = models.TextField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    Aadhar = models.TextField(null=True, blank=True)
    Pan = models.CharField(max_length=400,null = True , blank=True)
    Bank_Name = models.CharField(max_length=400, null= True, blank=True)
    Account_number = models.IntegerField(null = True, blank = True)
    IFSC = models.CharField(max_length=400, null= True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    Reference = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Reference', blank = True)
    location = models.ForeignKey(location, on_delete=models.CASCADE, null=True, related_name="location", blank=True)
    nominee1 = models.CharField(max_length=100, null=True, blank=True)
    Date_of_birth_nominee1 = models.DateField(null = True, blank=True)
    relation_with_nominee1 = models.CharField(max_length=100, null=True, blank=True)
    nominee2 = models.CharField(max_length=100, null=True, blank=True)
    Date_of_birth_nominee2 = models.DateField(null = True, blank=True)
    relation_with_nominee2 = models.CharField(max_length=100, null=True, blank=True)
    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.user) + '['+str(self.Aadhar)+']'

#############################################
from datetime import datetime, timedelta

def months_between_dates(start_date, end_date):
    current_date = start_date
    while current_date < end_date:
        yield current_date.strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM'
        # Move to the next month
        year = current_date.year + (current_date.month // 12)
        month = current_date.month % 12 + 1
        current_date = current_date.replace(year, month, 1)

##############################################


#   all logic is below 

##############################################

import os
import django
from django.conf import settings
# from .models import User, Payment

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KalyanFinalCut.settings")  

import os
from datetime import datetime
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'KalyanFinalCut.settings'
# application = get_wsgi_application()

if not django.apps.apps.ready:
    django.setup()

def pay_monthly():
    print("Function is running...")
    users = User.objects.all()

    if users.exists():
        for user in users:
            user_details = user.userdetails_set.all()

            if user_details.exists():
                # print("User exists:", user)
                # Create payment entries for different months
                for i in range(1, 2):
                    month = f'2022-04-01'
                    # print(f"Creating payment entry for {user} in {month}")
                    # Loop through user_details queryset
                    start = datetime(2022, 4, 30)  # Start date
                    end = datetime(2023, 12, 31)  # End date

                    for month in months_between_dates(start, end):
                        print(month)
                        for detail in user_details:
                            join_date = str(detail.Date_of_joining)
                            if str(month) > join_date:
                                Payment.objects.create(
                                    host=user,
                                    Month=month,
                                    Name=detail.Name,
                                    # Add other fields as needed
                                    Ac_No = detail.Membership_number
                                )
                                print(f"payment month {month} {user} and joining date {join_date}")
                            else:
                                (f"User details do not exist for before {month}:", user)

            else:
                print("User details do not exist for:", user)
    else:
        print("No users exist.")

# Call the function
pay_monthly()

##############################################

# records = Payment.objects.all()
# records.delete() 

