from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            "password": forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }
        fields = ['username', 'first_name', 'last_name', 'email', 'password']