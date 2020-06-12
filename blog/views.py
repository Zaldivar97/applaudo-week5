from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import BaseDetailView, TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment, CommentReport
from .forms import PostCreateForm


# Create your views here.

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        post = form.instance
        user = self.request.user
        post.user = user
        self.success_url = reverse('profile-index', kwargs={'id': user.profile.id})
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.approved = False
        self.success_url = reverse('profile-index', kwargs={'id': user.profile.id})
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'


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
        user = self.request.user
        post = self.get_object()
        owner = self.is_owner(user, post)
        user_like_exists, post_exist_in_list = self.check_user(user)
        context['like_exists'] = user_like_exists
        context['post_exist_in_list'] = post_exist_in_list
        context['owner'] = owner
        return context

    def is_owner(self, user, post):
        return user.id is post.user.id

    def verify_user_like(self, user):
        user_like_exists = self.object.like_by_user_exists(user)
        return user_like_exists

    def is_added_to_user_list(self, user):
        post_is_added = self.object.is_added_to_reading_list(user)
        return post_is_added

    def check_user(self, user):
        if user.is_authenticated:
            Comment.user_logged_id = user.id
            return (self.verify_user_like(user),
                    self.is_added_to_user_list(user)
                    )
        Comment.user_logged_id = None
        return False


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


class PostReadLater(LoginRequiredMixin, BaseDetailView):
    model = Post

    def post(self, *args, **kwargs):
        user = self.request.user
        post = self.get_object()
        post.reading_list.add(user)
        return HttpResponseRedirect(post.get_absolute_url())


class CommentLike(LoginRequiredMixin, BaseDetailView):
    model = Comment
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
        user = self.request.user
        comment = self.get_object()
        comment.likes.add(user.id)
        return HttpResponseRedirect(comment.post.get_absolute_url())


class Report(LoginRequiredMixin, TemplateResponseMixin, BaseDetailView):
    model = Comment
    template_name = 'blog/confirm-report.html'
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
        user = self.request.user
        comment = self.get_object()
        reason = self.request.POST.get('reason')
        comment_report = CommentReport(user=user, comment=comment, reason=reason)
        comment_report.save()
        return HttpResponseRedirect(comment.post.get_absolute_url())

# /posts/<slug>/like
