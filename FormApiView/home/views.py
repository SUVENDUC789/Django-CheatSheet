from django.shortcuts import render
from home.forms import StudentReg
# Create your views here.

def home(request):
    if request.method=='POST':
        f=StudentReg(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
    else:
        f=StudentReg()

    p={'form':f}
    return render(request,'home.html',p)
