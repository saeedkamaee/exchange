from .parent import Parent
from django.db import models
from .utillity import Gender

class staff(Parent):
    """ for recoroding infromation of the all staff"""
    name=models.CharField(max_length=200,blank=False)
    family=models.CharField(max_length=400,blank=False)
    national_code = models.CharField(max_length=1,unique=True)
    birthday = models.DateField()
    adress=models.TextField(blank=True)
    phone=models.CharField(max_length=12,unique=True)
    gender = models.CharField(max_length=15, choices=Gender.choices,default="2")
    email=models.EmailField()
