from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    data='''
    <a href="/myproject"> All Project <a> <hr>
    <a href="/lang"> Programming Language<a>
    
    '''
    return HttpResponse(data)
