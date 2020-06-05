from django.urls import path
from .views import LoginView, LogoutView, SignupView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('signup/', SignupView.as_view(), name='signup-view')

]
