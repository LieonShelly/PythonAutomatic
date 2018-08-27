from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def userLogin(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            cd = loginForm.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome You.")
            else:
                return HttpResponse('Invalid login')
    if request.method == "GET":
        loginForm = LoginForm()
        return render(request, "account/login.html",{"form": loginForm})

