from django.shortcuts import render
from home.forms import StudentsReg


def home(request):
    fm = StudentsReg()
    return render(request, 'home.html', {'form': fm})
