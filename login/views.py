from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from login.models import Users
from .forms import LoginForm, SignUpForm


def home(request):
    return render(request, 'index.html', {})


def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/success/')
    else:
        form = LoginForm()
    return render (request,'login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:

        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



