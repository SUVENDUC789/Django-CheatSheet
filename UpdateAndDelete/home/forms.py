from django import forms

class StudentReg(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your Name'})
    email=forms.EmailField(error_messages={'required':'Enter your Email'})