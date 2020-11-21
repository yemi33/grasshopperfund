from django.db import models

from ..organizations.models import Organization

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=300, unique=True)
    ##organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='tags', null=True)
    ##post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags', null=True)
    campaigns = models.ManyToManyField('campaigns.Campaign', related_name='tags', blank=True)

    def __str__(self): return f"#{self.name}"
