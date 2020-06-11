from django.contrib.auth.models import User
from django.db.models.signals import post_save

from profiles.models import Profile


# Create your models here.

def post_save_user(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except Exception:
            raise


post_save.connect(post_save_user, sender=User)
