from django.shortcuts import render
from .models import BlogArticles

def blogTitle(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})

def blogArticle(request, article_id):
    arttile = BlogArticles.objects.get(id=article_id)
    pub = arttile.publish
    return render(request, "blog/content.html", {"article": arttile, "publish": pub})
