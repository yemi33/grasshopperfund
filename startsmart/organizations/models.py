from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(default='campaign_default_pic.png', blank=True, upload_to='organization_pics')


    def __str__(self):
        return f"name: {self.name} \nowner: {self.owner} \ndescription:{self.description}"



class Post(models.Model):
    # Foreign keys
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='posts')

    # What should char limit be?
    text = models.TextField(max_length=1000)

    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"author: {self.author} \norganization: {self.organization} \ntext:{self.text}"
