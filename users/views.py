from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, ProfileForm, UpdateUserForm, UpdateProfileForm
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

def view_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    user_form = UpdateUserForm()
    profile_form = UpdateProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile' : profile
    }
    return render(request, 'users/profile.html', context)
