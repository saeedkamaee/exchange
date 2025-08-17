from django.db import models


from .parent import Parent



class Currency(Parent) : 
    name = models.CharField(max_length = 50,unique = True)
    symbol = models.CharField(max_length = 30,unique = True)
    is_active = models.BooleanField(default=True)
    