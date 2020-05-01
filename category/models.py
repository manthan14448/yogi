from django.db import models
from customer_info.models import *
# Create your models here.
class Product_Type(models.Model):
    product_type_id=models.AutoField(primary_key=True)
    product_type=models.CharField(max_length=50)
    def __str__(self):
        return self.product_type
class color(models.Model):
    colors=models.CharField(max_length=10)
    def __str__(self):
        return self.colors

class Product_View(models.Model):
    p_dis=models.CharField(max_length=10,null=True,default='none')
    product_type_id=models.ForeignKey(Product_Type,on_delete=models.SET_NULL,null=True)
    p_code=models.CharField(max_length=10,unique=True)
    p_img=models.ImageField(upload_to='pics')
    p_description=models.TextField()
    p_color=models.ForeignKey(color,on_delete=models.SET_NULL,null=True)
    p_weight=models.FloatField()
    p_price=models.FloatField()
    p_hight=models.FloatField()
    p_width=models.FloatField()
    def __str__(self):
        return self.p_code+' '+str(self.product_type_id)
class Custom_Product(models.Model):
    c_id=models.ForeignKey(customer_detail,on_delete=models.CASCADE,null=True,blank=True)
    p_code=models.CharField(max_length=10,null=True,blank=True,unique=True)
    p_type_id=models.CharField(max_length=10,null=True,blank=True)
    p_img=models.ImageField(upload_to='custom_pics',null=True,blank=True)
    p_description=models.TextField(null=True,blank=True)
    p_color=models.CharField(max_length=10,null=True,blank=True)
    p_price = models.FloatField(null=True,blank=True)
