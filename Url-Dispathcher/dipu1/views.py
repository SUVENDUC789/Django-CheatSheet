from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    data='''
    <a href="p1/"> Project 1 <a> <hr>
    <a href="p2/"> Project 2 <a> <hr>
    <a href="p3/"> Project 3 <a> <hr>   
    '''
    return HttpResponse(data)

def p2(request):
    data='''
    This is my Project 2  
    '''
    return HttpResponse(data)

def p1(request):
    data='''
    This is my Project 1  
    '''
    return HttpResponse(data)

def p3(request):
    data='''
    This is my Project 3  
    '''
    return HttpResponse(data)
