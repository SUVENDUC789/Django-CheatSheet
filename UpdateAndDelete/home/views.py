from django.shortcuts import render
from home.forms import StudentReg
from home.models import User
# Create your views here.

def home(request):
    if request.method=='POST':
        f=StudentReg(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            nm=f.cleaned_data['name']
            em=f.cleaned_data['email']

            # reg=User(id=3,name=nm,email=em)
            # reg.delete()

            reg=User(name=nm,email=em)
            reg.save()

            

            p={'form':f}
            return render(request,'home.html',p)
    else:
        f=StudentReg()

    p={'form':f}
    return render(request,'home.html',p)

def table(request):
    table=User.objects.all()
    # print(type(table))
    for i in table :
        print(i.name,i.email)

    return render(request,'table.html',{'data':table})