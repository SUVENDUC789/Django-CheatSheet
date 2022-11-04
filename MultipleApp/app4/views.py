from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def app4(request):
    return HttpResponse('<h1><a href="/app3/">Go to app4</a></h1>')
