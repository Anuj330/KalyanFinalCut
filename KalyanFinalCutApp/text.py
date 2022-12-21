# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class MonthlyPayments(models.Model):
#     name = models.ForeignKey(User, on_delete = models.SET_NULL, null=True )
#     Cheque_No = models.IntegerField(null = True , blank=True)
#     SM_Dr = models.IntegerField(null = True , blank=True)
#     SM_Cr = models.IntegerField(null = True , blank=True)
#     SM_Balance = models.IntegerField(null = True , blank=True)
#     CD_Dr = models.IntegerField(null = True , blank=True)
#     CD_Cr = models.IntegerField(null = True , blank=True)
#     CD_Balance = models.IntegerField(null = True , blank=True)
#     OD_Dr = models.IntegerField(null = True , blank=True)
#     OD_Cr = models.IntegerField(null = True , blank=True)
#     OD_Balance = models.IntegerField(null = True , blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     Date = models.DateTimeField(auto_now_add=True)
    
    

#     class Meta:
#         ordering = ['-Date', '-updated']

#     def __str__(self):
#         return str(self.name)


# class userDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     MonthlyPayment = models.ForeignKey(MonthlyPayments, on_delete=models.CASCADE) #SET_NULL to save the messages of the room\
#     Address = models.TextField()
#     Aadhar = models.IntegerField(null = True , blank=True)
#     Pan = models.IntegerField(null = True , blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return str(self.user)