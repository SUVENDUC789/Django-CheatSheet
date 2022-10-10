from django import forms

class StudentReg(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)
    def clean(self):
        cleaned_data=super().clean()
        valped=self.cleaned_data['password']
        valped2=self.cleaned_data['rpassword']
        if(valped!=valped2):
            raise forms.ValidationError('Password Not Matched')
