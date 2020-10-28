from django.db import models
from slugify import slugify
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)


    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title
