from django.db import models
from category.models import color
class PColor(models.Model):
    name=models.ForeignKey(color,on_delete=models.SET_NULL,null=True)
    price=models.IntegerField()
    def __str__(self):
        return str(self.name)
