from django.contrib import admin
from .models import *

@admin.register(Custom_Product)
class CustomProduct(admin.ModelAdmin):
    list_display=('c_id','p_code','p_type_id','p_img','p_description','p_color','p_price')
    list_editable = ('p_price','p_code')
    list_filter = ('p_type_id','c_id')
@admin.register(Product_View)
class ProductviewAdmin(admin.ModelAdmin):
    list_display = ('p_code','product_type_id','p_img','p_description','p_color','p_weight','p_hight','p_width','p_price')
    list_display_links = ('p_code','product_type_id')
    list_editable = ('p_price',)
    list_filter = ('product_type_id',)
    fieldsets =(
        (None,{
            'fields':(
                'p_code',
                'product_type_id',
                'p_img',
                'p_description',
                'p_color',
                'p_weight',
                'p_hight',
                'p_width',
                'p_price'
            )

         }),
    )
