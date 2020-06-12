from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class UserForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
