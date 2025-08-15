from .parent import Parent
from django.db import models


class staff(Parent):
    name=models.CharField(max_length=200,blank=False,)