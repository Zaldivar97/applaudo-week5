from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Confirm password'})

    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            'username': forms.fields.TextInput(attrs={'placeholder': 'Username'}),
        }

class LoginForm(AuthenticationForm):
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Password'})