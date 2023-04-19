from django.db import models
from django.contrib import admin
# Create your models here.
class Laptop(models.Model):
    Productid= models.CharField(max_length=100,primary_key = True)
    Brandname = models.CharField(max_length=100)
    Modelname = models.CharField(max_length=80)
    Price = models.IntegerField()
    Colour = models.CharField(max_length=100)

    
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('Productid','Brandname','Modelname','Price','Colour')