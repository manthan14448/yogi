from django.db import models

# Create your models here.
class employee_master(models.Model):
    e_id=models.AutoField(primary_key=True)
    e_name=models.CharField(max_length=10)
    e_add=models.CharField(max_length=100)
    e_con_no=models.IntegerField()
    e_desig=models.CharField(max_length=10)
    salary=models.IntegerField()
    def __str__(self):
        return self.e_name