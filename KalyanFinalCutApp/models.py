from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .choices import GENDER_TYPE_CHOICE

# Create your models here.

# def get_expiry():
#     return datetime.today() + timedelta(days=30)


class Payment(models.Model):
    host = models.ForeignKey(User, on_delete = models.CASCADE, null=True )
    Name = models.CharField(max_length=400, null= True,blank=True)
    # share_money = models.IntegerField(null = True , blank=True)
    Ac_No = models.IntegerField(null = True , blank=True, default= 0)
    Phone = models.IntegerField(null = True , blank=True, default= 0)
    Month = models.DateField(null = True, blank=True)
    Share_Money = models.FloatField(null = True , blank=True, default=0)
    Late_Charge = models.IntegerField(null = True , blank=True, default=0)
    Balance = models.FloatField(null = True , blank=True, default= 0)
    Loan = models.IntegerField(null = True , blank=True, default=0)
    Loan_Installment = models.IntegerField(null = True , blank=True, default=0)
    Loan_Interest = models.IntegerField(null = True , blank=True, default=0)
    Late_Loan_Charge = models.IntegerField(null = True , blank=True, default= 0)
    Loan_Balance = models.IntegerField(null = True , blank=True, default= 0)
    # Date = models.DateField(null = True, blank=True)

     
    def __str__(self):
        return str(self.host) +'['+str(self.Month)+']' + '['+str(self.Name)+']'


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


