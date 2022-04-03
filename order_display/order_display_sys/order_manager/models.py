from django.db import models

# Create your models here.
class Order(models.Model):
    order_ref = models.CharField(max_length=20)
    status = models.CharField(max_length=20)