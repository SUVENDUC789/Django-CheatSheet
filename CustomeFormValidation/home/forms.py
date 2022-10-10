# forms.py

from django import forms 

class StudentsReg(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    # password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
    #    cleaned_data = self.clean()
       valname=self.cleaned_data['name']
       valemail=self.cleaned_data['email']
    #    valemail=self.cleaned_data['password']
       if len(valname)<4:
            raise forms.ValidationError('Name shuld be more then equal 4')
       if len(valemail)<10:
            raise forms.ValidationError('Email shuld be more than or equal 10')

