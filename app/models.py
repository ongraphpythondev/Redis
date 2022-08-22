from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)