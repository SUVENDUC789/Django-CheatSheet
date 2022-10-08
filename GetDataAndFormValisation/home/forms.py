import email
from unicodedata import name
from django import forms

class StudentReg(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()