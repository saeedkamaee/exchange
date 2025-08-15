from django.db import models

class Parent(models.Model):
    creat_time=models.DateTimeField(auto_now_add=True)
    creat_update=models.DateTimeField(auto_now_add=True)
    description=models.TextField(blank=True)

    class Meta():
        abstract=True
        