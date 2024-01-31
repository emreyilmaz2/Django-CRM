from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
# from .models import Record


# Create your views here.

def home(request):
    # Check if someone is trying to log in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In Sir')
            return redirect('home')
        else:
            messages.success(request, "There Was Error Sir Please Give Me Ten(10) Pounds...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Cikis Yaptiniz!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
    return render(request, 'register.html', {})