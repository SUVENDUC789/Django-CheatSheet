from django.shortcuts import render,HttpResponseRedirect
from home.forms import StudentReg


def home(request):
    if request.method=='POST':
        f=StudentReg(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            print("Name : ",f.cleaned_data['name'])
            print("Email : ",f.cleaned_data['email'])
            print("Password : ",f.cleaned_data['password'])
            print("Agree : ",f.cleaned_data['agree'])
            print("Agree : ",f.cleaned_data['age'])
            p={'form':f}
            return render(request,'home.html',p)
    else:
        f=StudentReg()

    p={'form':f}
    return render(request,'home.html',p)