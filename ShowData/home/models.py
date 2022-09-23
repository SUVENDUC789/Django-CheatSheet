from django.db import models

# Create your models here.

class Biliniars(models.Model):
    brank=models.CharField(max_length=10)
    bname=models.CharField(max_length=100)
    bnetworth=models.CharField(max_length=100)
    bage=models.CharField(max_length=2)
    bsource=models.CharField(max_length=200)
    bcountry=models.CharField(max_length=50)