from django import forms

class StudentReg(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your Name'})
    # phone=forms.IntegerField(min_length=8)
    email=forms.EmailField(error_messages={'required':'Enter your Email'})
    password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput,error_messages={'required':'Enter Password'})
    age=forms.IntegerField()
    agree=forms.BooleanField(label='I agree')