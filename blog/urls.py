from django.urls import path
from .views import (PostListView, PostView, PostListPopular,
                    PostComment, PostLike, CommentLike, PostCreate)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreate.as_view(), name='post_new'),
    path('most-popular/', PostListPopular.as_view(), name='post_popular'),
    path('<slug>/', PostView.as_view(), name='post_detail'),
    path('<slug>/comments/', PostComment.as_view(), name='post_comment'),
    path('<slug>/likes/', PostLike.as_view(), name='post_like'),
    path('comments/<id>/like', CommentLike.as_view(), name='comment_like')

]
