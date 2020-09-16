from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def profile_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)

@receiver(post_save, sender=User)
def profile_saved(sender, instance, **kwargs):
    instance.profile.save()
