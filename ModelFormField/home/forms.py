from django import forms
from home.models import User

class StudentsReg(forms.ModelForm):
    class Meta:
        model=User
        # fields=['name','password','email']
        # fields='__all__'
        exclude=['password']