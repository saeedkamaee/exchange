from django.db import models

class Gender(models.TextChoices):
    FEMALE = "0", "Female"
    MALE = "1", "Male"
    OTHER = "2", "Other"





class Possion (models.TextChoices):
    Boss = "0", "Boss"
    Seller = "1", "Seller"
    Accountant= "2","Accountant"
    Cleaner="3","Cleaner"
    

class TypePic(models.TextChoices):
    Picture = "0", "Picture"
    Icon = "1", "Icon"
    Document="2","Document"
    OTHER = "3", "Other"



class TypeDeal(models.TextChoices):
    Sell = "0", "Sell"
    Buy = "1", "Buy"
   
