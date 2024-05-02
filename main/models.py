from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    created_by=models.CharField(max_length=100)
    created_at=models.DateField( auto_now_add=True)
    images=models.ImageField(upload_to='products/')
