from django.db import models


from .parent import Parent
from .branch import Branch
from .price import Price
from .staff import Staff
from .customer import Customer
from .utillity import TypeDeal


class Transaction (Parent):
    """Based on the Price and customer for recording all of Transaction"""
    price=models.ForeignKey(Price,on_delete=models.PROTECT)
    branch=models.ForeignKey(Branch,on_delete=models.PROTECT)
    staff=models.ForeignKey(Staff,on_delete=models.PROTECT)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
    type_deal = models.CharField(max_length=15, choices=TypeDeal.choices,default="0")
    date_transaction=models.DateTimeField(auto_now_add=True)
    

    class Meta:
            verbose_name_plural = "Price"
       
