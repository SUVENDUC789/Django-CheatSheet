from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')
def stu(request,id):
    return HttpResponse(f'<h1>Students - {id}</h1>')
