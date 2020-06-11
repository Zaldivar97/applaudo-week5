from django.urls import path

from .views import ProfileView, UpdateProfile

urlpatterns = [
 path('<id>/', ProfileView.as_view(), name='profile-index'),
 path('<id>/update', UpdateProfile.as_view(), name='profile-update')

]
