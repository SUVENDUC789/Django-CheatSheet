from django.shortcuts import render, HttpResponse
from home.forms import StudentReg
# Create your views here.


def home(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['email'])

    else:
        fm = StudentReg()
    return render(request, 'home.html', {'form': fm})
