from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post
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
