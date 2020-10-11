from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    target_money = models.IntegerField()
    current_money = models.IntegerField()
    days_left = models.IntegerField()
    num_of_backers = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

