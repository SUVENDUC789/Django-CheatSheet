from django.urls import path
from . import views
urlpatterns = [
    path('py/', views.home, name='home'),
]