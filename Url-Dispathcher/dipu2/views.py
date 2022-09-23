from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    data='''
    <a href="python/"> Python <a> <hr>
    <a href="java/"> Java <a> <hr>
    <a href="django/"> Django <a> <hr>
    <a href="php/"> Php <a> <hr>   
    '''
    return HttpResponse(data)

def p(request):
    data='''
    This is my python project  
    '''
    return HttpResponse(data)

def j(request):
    data='''
    This is my java project  
    '''
    return HttpResponse(data)

def d(request):
    data='''
    This is my django project  
    '''
    return HttpResponse(data)

def ph(request):
    data='''
    This is my php project  
    '''
    return HttpResponse(data)
