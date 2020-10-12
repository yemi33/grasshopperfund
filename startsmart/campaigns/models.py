from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    target_money = models.IntegerField()
    current_money = models.IntegerField()
    days_left = models.IntegerField()
    num_of_backers = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    search_fields = ['creator__username']

    class Meta:
        unique_together = (('creator','title'),)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
