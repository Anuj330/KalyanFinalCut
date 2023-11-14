from django.forms import ModelForm
from .models import userdetails, Payment

class userdettailsForm(ModelForm):
    # body = forms.charfield(required = True)
    
    class Meta:
        model = userdetails
        fields = ['user','Name', 'Date_of_birth', 'gender', 'Address' ,'Email', 'phone_number', 'Bank_Name', 'Account_number', 'IFSC', 'nominee1', 'nominee2'] 


class PaymentdetailsForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['Loan', 'Loan_Installment', 'Loan_Interest', 'Late_Loan_Charge', 'Loan_Balance']

        
    
