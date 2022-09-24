from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from home.forms import StudentReg
# Create your views here.

def submit(request):
    return render(request,'submit.html')

def home(request):
    if request.method=='POST':
        f=StudentReg(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            print("Name : ",f.cleaned_data['name'])
            print("Email : ",f.cleaned_data['email'])
            print("Password : ",f.cleaned_data['password'])
            # return render(request,'submit.html',{'name':f.cleaned_data['name']})
            return HttpResponseRedirect("/submit/")
    else:
        f=StudentReg()

    p={'form':f}
    return render(request,'home.html',p)
