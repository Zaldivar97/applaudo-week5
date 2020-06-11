from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_description = models.CharField(max_length=300)

    def comments_count(self):
        return self.user.comments.count()

    def likes_count(self):
        return self.user.likes.count()

    def posts(self):
        return self.user.posts

