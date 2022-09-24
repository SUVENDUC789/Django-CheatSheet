
### 1.Create Django Project:
```terminal
django-admin startproject PROJECTNAME
```
### **Run local server**
```terminal
py manage.py runserver
```

### **Run local server with another PORT**
```terminal
py manage.py runserver
```

### 2.Create Django App:
```terminal
py manage.py startapp APPNAME
```

### 3.Open settings.py file and add your app name in INSTALLED_APPS list  :
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'APPNAME', #----Add your app name 
]
```

### 4.Create templates folder in root directory:
### 5.Open settings.py file and after adding your app name then update TEMPLATES list  :
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],#---->Add folder name 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 6.Create static folder in root directory:
### 7.Open settings.py file and after adding  your app name then create this list   :
```python
STATICFILES_DIRS = [
        BASE_DIR,"static"
]
```

### 8.After update models.py file then run this command:
```terminal
py manage.py makemigrations
```

### 9.After run py manage.py makemigrations command then run this command :
```terminal
py manage.py migrate
```
### **Create forms.py file**
### And write some code:
```python
from django import forms

class StudentReg(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your Name'})
    # phone=forms.IntegerField(min_length=8)
    email=forms.EmailField(error_messages={'required':'Enter your Email'})
    password=forms.CharField(min_length=8,max_length=16,widget=forms.PasswordInput,error_messages={'required':'Enter Password'})
    age=forms.IntegerField()
    agree=forms.BooleanField(label='I agree')
```
### **Open views.py file And write some code**

```python
from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from home.forms import StudentReg
# Create your views here.

def submit(request):
    return render(request,'submit.html')

def home(request):
    if request.method=='POST':
        f=StudentReg(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            print("Name : ",f.cleaned_data['name'])
            print("Email : ",f.cleaned_data['email'])
            print("Password : ",f.cleaned_data['password'])
            print("Agree : ",f.cleaned_data['agree'])
            print("Agree : ",f.cleaned_data['age'])
            # return render(request,'submit.html',{'name':f.cleaned_data['name']})
            return HttpResponseRedirect("/submit/")
    else:
        f=StudentReg()

    p={'form':f}
    return render(request,'home.html',p)

```
### **Open home.html file And write some code**
```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form api in django</title>
</head>
<body>
    <h1>form api</h1>
    <form action="" method="post" novalidate>
        {% csrf_token %}

        <table>{{form}}</table>
        <input type="submit" value="submit">
    </form>
</body>
</html>

```
