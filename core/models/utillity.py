from django.db import models

class Gender(models.TextChoices):
    FEMALE = "0", "Female"
    MALE = "1", "Male"
    OTHER = "2", "Other"

    class Meta():
        abstract=True



class Possion (models.TextChoices):
    Boss = "0", "Boss"
    Seller = "1", "Seller"
    Accountant= "2","Accountant"
    Cleaner="3","Cleaner"
    
    class Meta():
        abstract=True 