from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(employee_master)
class empmaster(admin.ModelAdmin):
    list_display = ('e_name','e_desig','salary')
    list_display_links = ('e_desig',)
    list_editable = ('salary',)
    list_filter = ('e_desig',)