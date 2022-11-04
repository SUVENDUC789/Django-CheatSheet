from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2(request):
    return HttpResponse('<h1><a href="/app1/">Go to app1</a></h1>')
