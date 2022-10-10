from django.shortcuts import render
from home.forms import StudentsReg
# Create your views here.

def home(request):
    if request.method=='POST':
        fm=StudentsReg(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            print("Name : ",fm.cleaned_data['name'])
            print("Email : ",fm.cleaned_data['email'])
            # print("Password : ",fm.cleaned_data['password'])
        return render(request,'home.html',{'form':fm})
    fm=StudentsReg()
    return render(request,'home.html',{'form':fm})
