from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/templates/registration/register.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/templates/registration/login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        if 'update' in request.POST:
            user = request.user
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    return render(request, 'registration/profile.html')