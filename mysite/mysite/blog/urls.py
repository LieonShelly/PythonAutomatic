from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.blogTitle, name="blog"),
    path('<int:article_id>/', views.blogArticle, name="blog_detail")
]