from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    clgroll=models.CharField(max_length=5)
