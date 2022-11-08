# URL Pattern inside Application 

### inside project folder

```python
from django.contrib import admin
from django.urls import path,include #--->add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),  #---> use include
    path('service/',include('service.urls')),  #---> use include
]
```

### inside service application folder create urls.py file and write some code.
```python
from django.urls import path
from . import views
urlpatterns = [
    path('py/', views.home, name='home'),
]
```

### inside home application folder create urls.py file and write some code.
```python
from django.urls import path
from . import views
urlpatterns = [
    path('dj/', views.home, name='home'),
]
```
