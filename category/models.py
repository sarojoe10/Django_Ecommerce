from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    cat_image = models.ImageField(upload_to='images/categories',blank=True,default='default.jpg')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
