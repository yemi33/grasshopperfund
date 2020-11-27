from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ..organizations.models import Organization

class Post(models.Model):
    # Foreign keys
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # allows us to access an organization's posts
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='posts')

    # What should char limit be?
    text = models.TextField(max_length=1000)

    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse("view-post", args=(self.organization.name,self.id))

    def already_liked(self, user: User) -> bool:
        '''
        Check if user has already liked this post
        '''
        return (self.likes.filter(user=user).exists())

    def add_like(self, user: User):
        '''
        Add a like to post from user and return the like
        '''
        return PostLike.objects.create(post=self, user=user)

    def remove_like(self, user: User):
        '''
        Remove a user's like to this post
        '''
        PostLike.objects.get(post=self, user=user).delete()


    def like(self, user: User):
        '''
        Like post, or unlike if post as already been liked by user
        '''

        if self.already_liked(user):
            # Unlike if post already liked
            self.remove_like(user)

        else:
            self.add_like(user)

    def __str__(self):
        return f"author: {self.author} \norganization: {self.organization} \ntext:{self.text}"



class Like(models.Model):
    '''
    Base class for likes
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_entities')
    created = models.DateTimeField(auto_now=True)


class PostLike(Like):
    '''
    Class for likes for Posts
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    unique_together = (('user', 'post'),)
