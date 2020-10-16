from django import forms
from django.forms import TextInput

from . models import Registration

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Registration
        fields = ("first_name",'last_name', "email_id",'Birthday','gender','Password','phone_nu')
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name' ,'class' : "form-control"}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name','class': "form-control"}),
            'email_id': TextInput(attrs={'placeholder': 'Email ID','class': 'form-control'}),
            'Birthday': TextInput(attrs={'placeholder': 'Type Your Birthday YYYY/MM/DD','class': 'form-control'}),
            'gender' : forms.Select(attrs={"type":'Select','class': 'dropdown'}),
            'phone_nu': TextInput(attrs={'placeholder':'Phone NU.','class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={"type":"password",'placeholder':'Password','class':'form-control form-group','data-toggle':"password"})
        }