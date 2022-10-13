from django.shortcuts import render
from home.forms import StudentsReg
from home.models import User
# Create your views here.


def home(request):
    if request.method == 'POST':
        f = StudentsReg(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            print("Name : ", f.cleaned_data['name'])
            print("Email : ", f.cleaned_data['email'])
            return render(request, 'home.html', {'form': f})
            # return HttpResponseRedirect("/submit/")
    else:
        f = StudentsReg()

    p = {'form': f}
    return render(request, 'home.html', p)
