from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostQuerySet(models.QuerySet):
    def most_popular(self):
        return self.filter(likes__gt=25)


class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        qs = super(PostModelManager, self).all(
            *args, **kwargs).filter(active=True)
        return qs


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField()
    objects = PostModelManager()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment #{self.id}'


def pre_save_post(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug


pre_save.connect(pre_save_post, sender=Post)



