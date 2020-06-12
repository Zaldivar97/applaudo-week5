from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField


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
        qs = super().all(*args, **kwargs).filter(active=True)
        return qs


class Post(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name="posts"
    )
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(get_user_model(), related_name="likes", blank=True)
    reading_list = models.ManyToManyField(get_user_model(), related_name='reading_list')
    title = models.CharField(max_length=200)
    content = HTMLField()
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    objects = PostModelManager()

    def comments(self):
        return self.comment_set.all()

    def likes_count(self):
        return self.likes.all().count()

    def like_by_user_exists(self, user):
        return self.likes.filter(id=user.id).exists()

    def is_added_to_reading_list(self, user):
        return self.reading_list.filter(id=user.id).exists()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["id"]


class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Comment creator'
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.ManyToManyField(get_user_model(), related_name='comment_likes', blank=True)
    content = models.TextField()
    flags = models.ManyToManyField(get_user_model(), through='CommentReport')
    approved = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    user_logged_id = None

    def likes_count(self):
        return self.likes.all().count()

    def like_by_user_exists(self):
        if self.user_logged_id is not None:
            return self.likes.filter(id=self.user_logged_id).exists()

    def report_by_user_exists(self):
        if self.user_logged_id is not None:
            return self.flags.filter(id=self.user_logged_id).exists()

    def __str__(self):
        return f'By {self.user}'

    class Meta:
        ordering = ["id"]


class CommentReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.CharField(max_length=64)
    created_at = models.DateField(auto_now_add=True)


def pre_save_post(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug


pre_save.connect(pre_save_post, sender=Post)
