from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('p2/', views.p2, name='p2'),
    path('p1/', views.p1, name='p1'),
    path('p3/', views.p3, name='p3'),
]