from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('python/', views.p, name='p'),
    path('java/', views.j, name='j'),
    path('django/', views.d, name='j'),
    path('php/', views.ph, name='j'),

]