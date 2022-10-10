from django.shortcuts import render
from home.forms import StudentReg
# Create your views here.

def home(request):
    if request.method=='POST':
        f=StudentReg(request.POST)
        if f.is_valid():
            print("Name : ",f.cleaned_data['name'])
            print("Password : ",f.cleaned_data['password'])
            print("Re-Password : ",f.cleaned_data['rpassword'])
        return render(request,'home.html',{'form':f})
    if request.method=='GET':   
     f=StudentReg()
     return render(request,'home.html',{'form':f})
