from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView, DeleteView
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
    post = Post.objects.get(
        id = post_id
    )

    context = {
        'organization': organization,
        'post': post,
    }

    return render(request, 'posts/view_post.html', context)



class CreatePostView(LoginRequiredMixin, FormView):
    template_name = 'posts/create_post.html'
    form_class = PostForm
    success_url = 'posts/view'

    def post(self, request, organization_name:str):
        '''
        Check post request for valid form
        '''
        form = self.get_form()
        if form.is_valid():
            # get organization
            self.organization = Organization.objects.get(name=organization_name)
            messages.success(request, "Posted!")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        '''
        This method is called on valid form data on a POST request
        '''
        author = form.cleaned_data["author"]
        text = form.cleaned_data["text"]

        new_post = Post(
            author = author,
            organization = self.organization,
            text = text,
        )

        new_post.save()

        return redirect("view-organization", organization_name = self.organization.name)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    '''
    Uses Django built-in generic view
    '''
    model = Post

    fields = [
        "text"
    ]

    def get_object(self):
        '''
        Override the built-in get_object method
        '''
        return Post.objects.get(pk=self.kwargs['post_id'])

class DeletePostView(LoginRequiredMixin, DeleteView):
    '''
    Uses Django built-in generic view
    '''
    model = Post

    def get_success_url(self):
        '''
        Redirect to the post's organization after deletion
        '''
        return self.get_object().organization.get_absolute_url()

    def get_object(self):
        '''
        Override the built-in get_object method
        '''
        return Post.objects.get(pk=self.kwargs['post_id'])
