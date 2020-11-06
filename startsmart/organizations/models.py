from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
