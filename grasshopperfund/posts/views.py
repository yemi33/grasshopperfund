from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..organizations.models import Organization

from .forms import PostForm
from .models import Post



def view_post(request, organization_name: str, post_id: str):
    '''
    View a single post
    '''

    organization = Organization.objects.get(
        name = organization_name
    )

    # Get post from the organization's posts
    post = Organization.posts.get(
        id = post_id
    )

    context = {
        'organization': organization,
        'post': post,
    }

    return render(request, 'posts/view_post.html')
