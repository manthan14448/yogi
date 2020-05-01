from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(customer_detail)
class cumdetail(admin.ModelAdmin):
    search_fields = ('c_id','c_name')
    list_display = ('c_name','c_id','e_mail','c_add','com_name','com_per_no')
    list_display_links = ('e_mail',)
    list_filter = ('c_name',)
@admin.register(customer_order)
class custorder(admin.ModelAdmin):
    list_display = ('o_id','c_id','order_date','d_status','pay_status','order_completion','totel_amt')
    list_editable = ('d_status','pay_status','order_completion')
    list_filter = ('c_id','o_id','order_date','d_status')
@admin.register(Inquery_order)
class Inquery_orders(admin.ModelAdmin):
        list_display = ('c_id','c_no', 'i_type','i_img','i_color', 'c_Description','qty','a_Description','a_status','price')
        list_editable = ('c_no','a_Description','a_status','price')
@admin.register(order_detail)
class orderdetail(admin.ModelAdmin):
    list_display = ('o_id', 'p_id','order_date','p_color', 'qty', 'price', 'pay_price', 'rate')
    list_editable = ('pay_price',)
    list_filter = ('o_id','p_id','order_date')
@admin.register(delivery)
class deliver(admin.ModelAdmin):
    list_display_links = ('d_add',)
    list_display = ('o_id', 'e_id', 'd_add', 'd_amt', 'pay_price', 'pay_status','d_complete')
    list_editable = ('e_id','d_amt', 'pay_price', 'pay_status', 'd_complete')
    list_filter = ('o_id','e_id','pay_status')

