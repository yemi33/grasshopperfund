from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    REQUIRED_FIELDS = ('user')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    interested_tags =  models.ManyToManyField('tags.Tags',related_name="interested_users", blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
