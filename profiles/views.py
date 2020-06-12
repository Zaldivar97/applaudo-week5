from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm, forms

from .models import Profile


# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/index.html'
    pk_url_kwarg = 'id'


class UserForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None


class ProfileForm(forms.Form):
    username = forms.CharField(label='', required=True)
    email = forms.EmailField(label='', required=False)
    profile_description = forms.CharField(label='', required=True)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profiles/update_profile.html'
    pk_url_kwarg = 'id'
    fields = ['profile_description']

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_form = UserForm(instance=user)
        context['user_form'] = user_form
        return context

    def post(self, *args, **kwargs):
        user = self.request.user
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        form = UserForm(dict(username=username, email=email), instance=user)
        if form.is_valid():
            form.save()
            return super().post(*args, **kwargs)
