from django.db import models
from slugify import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_list_by_category', args=[self.slug])


class Article(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id, self.slug])

    @classmethod
    def search_by_name(cls, search_term):
        search_result = cls.objects.filter(name__icontains=search_term)
        return search_result


class AccessoriesCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'accesscategory'
        verbose_name_plural = 'accessories_categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_list_by_category', args=[self.slug])


class Accessories(models.Model):
    accessoriescategory = models.ForeignKey(AccessoriesCategory, related_name='products', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Accessories, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', args=[self.id, self.slug])

    @classmethod
    def search_by_name(cls, search_term):
        search_result = cls.objects.filter(name__icontains=search_term)
        return search_result
