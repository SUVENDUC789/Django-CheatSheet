from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
        labels={'email':'Email'}


