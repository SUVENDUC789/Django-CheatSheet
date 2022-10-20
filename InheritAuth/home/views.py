from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(r):
    if r.method == 'POST':
        fm=SignUpForm(r.POST)
        if fm.is_valid():
            messages.success(r,'Your account create successfully !!')
            fm.save()
    else:
        fm=SignUpForm()
    return render(r,'home.html',{'form':fm})
