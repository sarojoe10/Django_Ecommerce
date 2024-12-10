from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    
