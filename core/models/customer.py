from .parent import Parent
from django.db import models
from .utillity import Gender


class Customer(Parent):
    """ for recoroding infromation aboout customer"""
    name=models.CharField(max_length=200,blank=False)
    family=models.CharField(max_length=400)
    national_code = models.CharField(max_length=1,unique=True)
    gender = models.CharField(max_length=15, choices=Gender.choices,default="2")
    birthday = models.DateField()
    adress=models.TextField(blank=True)
    phone=models.CharField(max_length=12,unique=True)
    