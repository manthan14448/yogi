from django.db import models
from customer_info.models import *
# Create your models here.
class customer_receipt(models.Model):
    r_id=models.CharField(max_length=64,null=True,blank=True)
    o_id=models.ForeignKey(customer_order,on_delete=models.SET_NULL,null=True,blank=True)
    c_id=models.ForeignKey(customer_detail,on_delete=models.SET_NULL,null=True,blank=True)
    c_email=models.CharField(max_length=30,null=True,blank=True)
    c_mobile=models.CharField(max_length=13,null=True,blank=True)
    d_id=models.ForeignKey(delivery,on_delete=models.SET_NULL,null=True,blank=True)
    c_amt=models.CharField(max_length=10,help_text='totle amount of money',null=True,blank=True)
    def __str__(self):
        return str(self.o_id)