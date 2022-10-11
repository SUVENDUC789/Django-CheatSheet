from django import forms

class StudentReg(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your Name'})
    phone=forms.CharField(min_length=8)
    email=forms.EmailField(error_messages={'required':'Enter your Email'},min_length=10)
    password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput,error_messages={'required':'Enter Password'})
    age=forms.IntegerField(error_messages={'required':'Enter your age'})
    agree=forms.BooleanField(label='I agree')