from django.contrib import admin
from .models import Article, Category, AccessoriesCategory, Accessories

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(AccessoriesCategory)
admin.site.register(Accessories)
