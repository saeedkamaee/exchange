from django.db import models


from .parent import Parent
from .branch import Branch
from .currency import Currency



class Price(Parent):
    """Based on the currency and branch model"""
    currency=models.ForeignKey(Currency,on_delete=models.PROTECT)
    branch=models.ForeignKey(Branch,on_delete=models.PROTECT)
    buy_price=models.DecimalField(max_digits=20,decimal_places=2,default=0.00)
    sell_price=models.DecimalField(max_digits=20,decimal_places=2,default=0.00)
    date_price=models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name_plural = "Price"
       
