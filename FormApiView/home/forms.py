from django import forms

class StudentReg(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)