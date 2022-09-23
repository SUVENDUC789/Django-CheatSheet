from django.shortcuts import render
from home.models import Biliniars
# Create your views here.

def home(request):
    e=Biliniars.objects.all()
    print(e)
    p={'bilname':e}
    return render(request,'home.html',p)
