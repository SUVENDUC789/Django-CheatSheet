from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<a href="/dj">next </a>')

def dj1(request):
    return HttpResponse('<a href="/"> Home </a>')