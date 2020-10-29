from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category

# Create your views here.


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    articles = Article.objects.all()[:4]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)
    return render(request, 'index.html', {'category': category, 'categories': categories, 'articles': articles})


def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    categories = Category.objects.all()
    return render(request, 'article_detail.html', {'article':article, 'categories': categories})


def all_news(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    articles = Article.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)
    return render(request, 'all_news.html', {'category': category, 'categories': categories, 'articles': articles})