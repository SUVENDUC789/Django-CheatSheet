# Multiple Application inside Project and their Function Based Views in Django

```python
from django.contrib import admin
from django.urls import path

from app1 import views as a1
from app2 import views as a2

from app3.views import app3
from app4.views import app4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a1.home, name='home'),
    path('app1/', a1.app1, name='app1'),
    path('app2/', a2.app2, name='app2'),
    path('app3/', app3, name='app3'),
    path('app4/', app4, name='app4'),
]
```