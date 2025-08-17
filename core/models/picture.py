from .parent import Parent
from django.db import models

from .utillity import TypePic
from .branch import Branch
from .customer import Customer
from .staff import Staff


class Picture(Parent):
    """ for save all of picture in exchange """
    name=models.CharField(max_length=200,blank=False)
    type_pic = models.CharField(max_length=15, choices=TypePic.choices,default="0")
    image = models.ImageField(upload_to='products/')
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT,null=True,blank=True)
    staff=models.ForeignKey(Staff,on_delete=models.PROTECT,null=True,blank=True)
    branch=models.ForeignKey(Branch,on_delete=models.PROTECT,null=True,blank=True)
    