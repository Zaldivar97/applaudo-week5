from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.detail import BaseDetailView, TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm, forms

from .models import Profile


# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/index.html'
    pk_url_kwarg = 'id'


class UpdateProfile(LoginRequiredMixin, TemplateResponseMixin, BaseDetailView):
    model = Profile
    template_name = 'profiles/update_profile.html'
    pk_url_kwarg = 'id'
