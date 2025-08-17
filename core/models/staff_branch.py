from django.db import models
from django.core.exceptions import ValidationError

from .parent import Parent
from .staff import Staff
from .branch import Branch
from .utillity import Possion


class StaffBranch(Parent):
    """ for creat relationship between staff and brach"""
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    Branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    possion = models.CharField(max_length=15, choices=Possion.choices,default="1")
    startdate=models.DateField()
    solary=models.DecimalField(max_digits=20,decimal_places=2,default=0.00)
    
    class Meta:
        unique_together = [
            ['staff', 'Branch', 'position']  # جلوگیری از ثبت تکراری
            ['branch', 'position'] 
            ]
        verbose_name_plural = "StaffBranches"
        
        def clean(self):
        # اعتبارسنجی سفارشی برای محدودیت "هر شعبه یک رئیس"
            if self.position == "Boss":
                existing_boss = StaffBranch.objects.filter(
                    branch=self.branch,
                    position="Boss"
                ).exclude(pk=self.pk).first()  # exclude برای موارد ویرایش
                
                if existing_boss:
                    raise ValidationError(
                        f"شعبه {self.branch} هم‌اکنون رئیس دارد: {existing_boss.staff}"
                    )

        def save(self, *args, **kwargs):
            self.full_clean()  # تضمین اجرای اعتبارسنجی‌ها قبل از ذخیره
            super().save(*args, **kwargs)
