from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=300, unique=True)
    campaigns = models.ManyToManyField('campaigns.Campaign', related_name='tags', blank=True)

    def __str__(self): return f"{self.name}"
