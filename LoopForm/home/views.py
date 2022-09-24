from django.shortcuts import render
from home.forms import StudentsReg
# Create your views here.

def home(request):
    if request.method == 'POST':
        s=StudentsReg(request.POST)
        print(s)
        if s.is_valid() :
            print("Form is valid")
            print("Name : ",s.cleaned_data['name'])
            print("Email : ",s.cleaned_data['email'])
            print("Password : ",s.cleaned_data['password'])
        # s=StudentsReg()
    else:
        s=StudentsReg()

    p={'form':s}
    return render (request,'home.html',p)

