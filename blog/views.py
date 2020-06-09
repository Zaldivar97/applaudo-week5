from django import template
from django.views.generic import DetailView, ListView, View
from django.views.generic.detail import SingleObjectMixin, BaseDetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Post, Comment, User


# Create your views here.


class PostListPopular(ListView):
    model = Post
    template_name = 'blog/posts.html'

    def get_queryset(self):
        return super().get_queryset().most_popular()


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            queryset = Post.objects.filter(title__icontains=query)
            return queryset
        return super().get_queryset()


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_like_exists = False
        if self.request.user.is_authenticated:
            user = self.request.user
            user_like_exists = self.object.like_by_user_exists(user)
            Comment.user_logged_id = user.id
        else:
            Comment.user_logged_id = None
        context['like_exists'] = user_like_exists
        return context


class PostComment(LoginRequiredMixin, BaseDetailView):
    model = Post
    permission_denied_message = 'You have to login'

    def post(self, *args, **kwargs):
        user = self.request.user
        content = self.request.POST['comment']
        comment = Comment(
            user=user,
            post=self.get_object(),
            content=content
        )
        comment.save()
        return HttpResponseRedirect(self.get_object().get_absolute_url())


class PostLike(LoginRequiredMixin, BaseDetailView):
    model = Post
    permission_denied_message = 'You have to login'

    def post(self, *args, **kwargs):
        user = self.request.user
        post = self.get_object()
        post.likes.add(user.id)
        return HttpResponseRedirect(post.get_absolute_url())


class CommentLike(LoginRequiredMixin, BaseDetailView):
    model = Comment
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
        user = self.request.user
        comment = self.get_object()
        comment.likes.add(user.id)
        return HttpResponseRedirect(comment.post.get_absolute_url())

# /posts/<slug>/like
