from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1(request):
    return HttpResponse('<h1><a href="/app2/">Go to app2</a></h1>')

def home(request):
    data='''
    <h1><a href="/app1/">Go to app1</a></h1><br>
    <h1><a href="/app2/">Go to app2</a></h1><br>
    <h1><a href="/app3/">Go to app3</a></h1><br>
    <h1><a href="/app4/">Go to app4</a></h1><br>
    '''
    return HttpResponse(data)
