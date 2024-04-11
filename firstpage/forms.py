from django import forms
from .models import PGForm,PGdetails
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm

class PGModelForm(forms.ModelForm):
    class Meta:
        model = PGForm
        fields='__all__'
class PGdetailsModelForm(forms.ModelForm):
    class Meta:
        model = PGdetails
        fields='__all__'
class  RegisterPg(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name', 'last_name', 'email', 'password1', 'password2']

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=['name']
class RegisterUser(UserCreationForm):
    '''phone_number = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'custom-class',
            'placeholder': 'Enter your Phone Number'
        }))'''
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'custom-class','placeholder': 'User Name'}),
            'first_name': forms.TextInput(attrs={'class': 'custom-class','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'custom-class','placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'custom-class','placeholder': 'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'custom-class','placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'custom-class','placeholder': 'Confirm Password'}),
        }
