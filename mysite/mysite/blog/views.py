from django.shortcuts import render
from .models import BlogArticles

def blogTitle(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})