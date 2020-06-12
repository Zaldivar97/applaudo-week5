from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_description = models.CharField(max_length=300, default='My profile description')

    def comments_count(self):
        return self.user.comments.count()

    def likes_count(self):
        return self.user.likes.count()

    def posts(self):
        return self.user.posts

    def get_absolute_url(self):
        return reverse('profile-index', kwargs={'id':self.id})
