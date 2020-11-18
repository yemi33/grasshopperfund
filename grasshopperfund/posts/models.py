from django.db import models
from django.contrib.auth.models import User

from ..organizations.models import Organization

class Post(models.Model):
    # Foreign keys
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # allows us to access an organization's posts
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='posts')

    # What should char limit be?
    text = models.TextField(max_length=1000)

    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"author: {self.author} \norganization: {self.organization} \ntext:{self.text}"
