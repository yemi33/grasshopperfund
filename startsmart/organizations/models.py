from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):

    # only one owner in current implementation
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')

    # Organization names must be unique
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)

    # main image to be used for the organization
    image = models.ImageField(default='campaign_default_pic.png', blank=True, upload_to='organization_pics')

    # automatically set creation date
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name} \nowner: {self.owner} \ndescription:{self.description}"

    @property
    def num_of_posts(self) -> int:
        return len(self.posts.all())


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
