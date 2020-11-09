from django.db import models

from startsmart.organizations.models import Organization, Post
from startsmart.campaigns.models import Campaign

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=300, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='tags', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags', null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='tags', null=True)

    def __str__(self): return f"name: {self.name}\n organization: {self.organization}\n campaign: {self.campaign}\n"
