from django.db import models
from django.db.models import Model


class  home(models.Model):
    product_name=models.CharField(max_length=15,default='')
    img= models.ImageField(upload_to='pics')
    price=models.IntegerField(max_length=10)
    offer=models.BooleanField(default=False)

