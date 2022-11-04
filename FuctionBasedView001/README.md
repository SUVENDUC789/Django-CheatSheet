# 1. Import HttpResponse class from django.http module

```python
from django.shortcuts import render
from django.http import HttpResponse #-----> this class we import that
# Create your views here.

def home(request):
    return HttpResponse('<a href="/dj">next </a>')

def dj1(request):
    return HttpResponse('<a href="/"> Home </a>')
```

