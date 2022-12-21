from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

# def get_expiry():
#     return datetime.today() + timedelta(days=30)


class Payment(models.Model):
    host = models.ForeignKey(User, on_delete = models.CASCADE, null=True )
    S_no = models.IntegerField(null=True, blank=True)
    Name = models.CharField(max_length=400, null= True)
    # share_money = models.IntegerField(null = True , blank=True)
    Ac_No = models.IntegerField(null = True , blank=True)
    Phone = models.IntegerField(null = True , blank=True)
    Month = models.DateField(null = True , blank=True)
    Share_Money = models.IntegerField(null = True , blank=True)
    Late_Charge = models.IntegerField(null = True , blank=True)
    Balance = models.IntegerField(null = True , blank=True)
    Loan = models.IntegerField(null = True , blank=True)
    Loan_Installment = models.IntegerField(null = True , blank=True)
    Loan_Interest = models.IntegerField(null = True , blank=True)
    Late_Loan_Charge = models.IntegerField(null = True , blank=True)
    Loan_Balance = models.IntegerField(null = True , blank=True)
    # Date = models
    # last_date = models.DateField(default=get_expiry)
    # updated = models.DateTimeField(auto_now=True, null = True)
    # created = models.DateField()
    # class Meta:
    #     ordering = ['-updated', '-created']


    # late_fee_share_money = models.IntegerField(default=late_free_share)
     
    def __str__(self):
        return str(self.host) +'['+str(self.Month)+']' + '['+str(self.Name)+']'


class userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_pay = models.ForeignKey(Payment, on_delete=models.CASCADE) #SET_NULL to save the messages of the room\
    Address = models.TextField()
    Aadhar = models.IntegerField(null = True , blank=True)
    Pan = models.IntegerField(null = True , blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.user) + '['+str(self.Aadhar)+']'


