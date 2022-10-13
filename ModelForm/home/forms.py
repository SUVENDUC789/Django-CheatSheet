from django import forms
from home.models import User
class StudentsReg(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter your name','email':'Enter Email'}
        error_messages={'name':{'required':'Your name is requeired please enter tour name'}}

        widgets={
            'password':forms.PasswordInput
        }
