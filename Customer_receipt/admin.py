from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(customer_receipt)
class Customerreceipt(admin.ModelAdmin):
    list_display = ('r_id','o_id','d_id','c_id','c_mobile','c_email','d_id','c_amt')
    list_filter = ('r_id','c_id','o_id')