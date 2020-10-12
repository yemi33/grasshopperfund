from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, ProfileForm, UpdateProfileForm
from .models import Profile
# Create your views here.

@login_required
def home_page(request):
    context = {}
    return render(request, 'users/home_page.html', context)

def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Registered!')
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, 'Logged in Successfully!')
            login(request, user)
            return redirect('startsmart-home')
    return render(request, 'users/login_page.html')

def logout_page(request):
    messages.success(request, 'Logged out Successfully!')
    logout(request)
    return render(request, 'users/logout_page.html')

@login_required
def view_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {
        'profile' : profile
    }
    return render(request, 'users/profile.html', context)

@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            messages.success(request, 'Profile Updated!')
            form.save()
            return redirect('update-profile')
    context = {
        'form': form
    }
    return render(request, 'users/update_profile.html', context)

@login_required
def delete_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile Deleted!')
        return redirect('register')

    return render(request, 'users/delete_profile.html')
