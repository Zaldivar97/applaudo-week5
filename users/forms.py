from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
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
