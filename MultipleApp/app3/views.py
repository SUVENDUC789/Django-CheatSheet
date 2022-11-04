from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app3(request):
    return HttpResponse('<h1><a href="/app4/">Go to app3</a></h1>')