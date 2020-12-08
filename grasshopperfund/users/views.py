from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView, DeleteView

from .forms import CreateUserForm, ProfileForm, UpdateProfileForm, AddInterestedTagsForm
from .models import Profile
from ..campaigns.models import Campaign, Donation

from ..tags.models import Tag
from ..posts.models import Post


from ..templates import *
# Create your views here.

def home_page(request):

    # init posts
    posts = None

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

        interested_orgs = set()

        for tag in profile.interested_tags.all():
            for campaign in tag.all_campaigns:
                interested_orgs.add(campaign.organization)

        # ordering already defaults to newest posts first
        posts = Post.objects.filter(organization__in=interested_orgs)

    # if user is not logged in, show all posts
    else:
        posts = Post.objects.all()


    campaigns = Campaign.objects.all()

    context = {
        'interested_posts': posts,
        'campaigns': campaigns,
    }
    return render(request, 'users/home_page.html', context)

def faq(request):
    campaigns = Campaign.objects.all()

    context = {
        'campaigns': campaigns,
    }

    return render(request, 'users/faq.html', context)

def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Registered!')
            form.save()

            # login the user
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request,new_user)

            # redirect to add interested tags
            return redirect('add-interested-tags')
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
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'users/login_page.html')

def logout_page(request):
    messages.success(request, 'Logged out Successfully!')
    logout(request)
    return render(request, 'users/logout_page.html')

@login_required
def view_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    donations = Donation.objects.all().filter(donor=profile.user)

    context = {
        'profile' : profile,
        'donations': donations,
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


class AddInterestedTagsView(LoginRequiredMixin, UpdateView):
    '''
    Uses Django built-in generic view
    '''
    model = Profile
    form_class = AddInterestedTagsForm

    # On success, direct to home page
    # In the future, probably direct to recommended campaigns
    success_url = '/'

    def get_object(self):
        '''
        Override the built-in get_object method
        '''
        return Profile.objects.get(
            user__id = self.request.user.id
        )
