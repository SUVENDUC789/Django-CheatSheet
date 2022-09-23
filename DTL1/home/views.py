from django.shortcuts import render

# Create your views here.

def home(request):
    p={
        'title':'DTL-Dynamic Template Files',
        'Creater':'Suvendu Chowdhury',
        'FrameWrok':'Django',
        'langu':'Python',
    }
    return render(request,'home.html',p)