from .parent import Parent
from django.db import models
from django.contrib.gis.db import models


class brach(Parent):
    """ for recoroding infromation about branchs of exchange """
    name=models.CharField(max_length=400,blank=False)
    adress=models.TextField(blank=True)
    phone=models.CharField(max_length=15)
    is_active = models.BooleanField (default=True,help_text="for checking activaty of brach")
    point=models.PointField()
    
    