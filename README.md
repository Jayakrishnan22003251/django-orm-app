# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Fork and clone the repositary in to your IDE.
### STEP 2:
Create a django project and an app and a superuser account and run the server.

### STEP 3:
Modify changes in settings and write ur code on models and admin and run the server.
### STEP 4:
Login in to admin using your superuser account and populate the records.
## PROGRAM:
```
from django.db import models
from django.contrib import admin
class Laptop(models.Model):
    Productid= models.CharField(max_length=100,primary_key = True)
    Brandname = models.CharField(max_length=100)
    Modelname = models.CharField(max_length=80)
    Os = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    Price = models.IntegerField()

    
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('Productid','Brandname','Modelname','Os','Colour','Price')
```
## OUTPUT:
![](/django-orm-app/j1.png)![j1](https://user-images.githubusercontent.com/120232371/233100340-7d9180a3-40ad-4df0-bbe8-96ae6cde7068.png)

## RESULT:
Thus we developed a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
