from django.conf.urls import url
from django.urls import path
from .import views

app_name = 'account'
urlpatterns = [
    path('login/', views.userLogin, name='userLogin')
]