from django.shortcuts import render
from home.forms import StudentsReg
# Create your views here.

def home(request):
    fm=StudentsReg(
        initial={'name':'Your Name','email':'email@gmail.com','dob':'You Dob'}
    )

    return render(request,'home.html',{'form':fm})
