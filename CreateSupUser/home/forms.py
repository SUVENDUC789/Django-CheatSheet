from django import forms

class StudentsReg(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    dob=forms.DateField()