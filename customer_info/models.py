from django.db import models
from category.models import *
from employee_master.models import *
# Create your models here.
class ppid(models.Model):
    pstatus=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.pstatus
class customer_detail(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=50)
    password=models.CharField(max_length=32)
    e_mail=models.EmailField()
    c_add=models.TextField(max_length=100)
    com_name=models.CharField(max_length=20,verbose_name='comapany name',blank=True,null=True,default=None)
    com_per_no=models.CharField(max_length=10,verbose_name='comapany person mobile-no',null=True,help_text="mobile_no if customer is not company")
    def __str__(self):
        return self.c_name+'  '+str(self.c_id)

class customer_order(models.Model):
    o_id=models.AutoField(primary_key=True)
    c_id=models.ForeignKey(customer_detail,on_delete=models.SET_NULL,null=True)
    order_date=models.DateField(null=True,blank=True)
    d_status=models.CharField(max_length=5)
    pay_status=models.ForeignKey(ppid,on_delete=models.SET_NULL,null=True,blank=True)
    order_completion = models.DateField(null=True, blank=True)
    totel_amt=models.CharField(max_length=10,help_text="totel amount of product",blank=True)
    def __str__(self):
        return str(self.o_id)
class Inquery_order(models.Model):
    c_id=models.ForeignKey(customer_detail,on_delete=models.CASCADE,null=True,blank=True)
    i_img=models.ImageField(null=True,upload_to='inq_pic',blank=True)
    i_type=models.CharField(max_length=20,blank=True,null=True)
    i_color=models.CharField(max_length=20,blank=True,null=True)
    c_no=models.CharField(max_length=10,unique=True,blank=True,null=True)
    c_Description=models.CharField(max_length=200,null=True,blank=True)
    a_Description = models.CharField(max_length=200, null=True,blank=True)
    qty=models.IntegerField(null=True,blank=True)
    a_status = models.BooleanField(null=True,blank=True)
    price=models.CharField(max_length=10,blank=True,null=True)
class order_detail(models.Model):
    o_d_id = models.AutoField(primary_key=True)
    o_id = models.ForeignKey(customer_order, on_delete=models.CASCADE, null=True)
    p_id = models.CharField(max_length=100, null=True,blank=True)
    p_color=models.CharField(max_length=20,null=True,blank=True)
    qty = models.IntegerField(null=True,blank=True)
    order_date=models.DateField(null=True,blank=True)
    price=models.CharField(max_length=20,null=True,blank=True)
    pay_price = models.BooleanField( null=True, blank=True)
    rate = models.CharField(max_length=10,help_text='the totel amount of product')
    def __str__(self):
        return str(self.o_id)+" "+str(self.p_id)
class delivery(models.Model):
    d_id=models.AutoField(primary_key=True)
    o_id=models.ForeignKey(customer_order,on_delete=models.CASCADE,null=True,blank=True)
    e_id=models.ForeignKey(employee_master,on_delete=models.SET_NULL,null=True,blank=True)
    d_add=models.TextField(max_length=120,null=True,default='none',blank=True)
    d_amt=models.CharField(max_length=10,blank=True)
    pay_price = models.CharField(max_length=20, null=True, blank=True)
    pay_status = models.ForeignKey(ppid, on_delete=models.SET_NULL, null=True,blank=True)
    d_status=models.CharField(max_length=10,blank=True,null=True)
    d_complete=models.BooleanField(blank=True,null=True)
    def __str__(self):
        return str(self.o_id)+" "+str(self.d_status)