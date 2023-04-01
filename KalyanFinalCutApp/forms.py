from django.forms import ModelForm
from .models import userdetails

class userdettailsForm(ModelForm):
    # body = forms.charfield(required = True)
    
    class Meta:
        model = userdetails
        fields = ['Name','Address', 'Aadhar','Pan', 'Bank_Name', 'Account_number','IFSC' ]
        
        
    
