from django.db import models
from customer_info.models import *
# Create your models here.
class customer_img(models.Model):
    img_id=models.ForeignKey(customer_detail,on_delete=models.CASCADE,null=True,blank=True)
    c_img=models.ImageField(upload_to='user_pics',null=True,blank=True)
    def __str__(self):
        return str(self.img_id)
class temp_cart(models.Model):
    c_id=models.TextField(max_length=20)
    p_name=models.TextField(max_length=20,null=True,blank=True)
    modifiction=models.TextField(max_length=20,null=True,blank=True)
    p_id=models.TextField(max_length=20,null=True,blank=True)
    qty=models.TextField(max_length=3,null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    Totel=models.FloatField(null=True,blank=True)
    def __str__(self):
        return str(self.id)