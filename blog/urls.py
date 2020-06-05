from django.urls import path
from .views import PostListView, PostView, PostListPopular

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('most-popular/', PostListPopular.as_view(), name='post_popular'),
    path('<slug>/', PostView.as_view(), name='post_detail')
]
