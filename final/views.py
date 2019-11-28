from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request,'home.html')

def novo_login(request):
    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Seja bem vindo!')
            return redirect( '/prova/home/')

        else:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha incorreto!')
    return render (request, 'login.html')
