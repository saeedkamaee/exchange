from .parent import Parent
from django.db import models  


class Branch(Parent):
    """ for recoroding infromation about branchs of exchange """
    name=models.CharField(max_length=400,blank=False)
    adress=models.TextField(blank=True)
    phone=models.CharField(max_length=15)
    is_active = models.BooleanField (default=True,help_text="for checking activaty of brach")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    def __str__(self):
        return self.name
    