
### 1.Create Django Project:
```terminal
django-admin startproject PROJECTNAME
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









