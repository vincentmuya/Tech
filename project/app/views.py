from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category

# Create your views here.


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    return render(request, 'index.html', {'categories': categories, 'articles': articles})
