from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


# Create your tests here.
class ViewTest(TestCase):
    c = Client()

    def test_profile_not_loggued_in(self):
        response = self.c.get(
            reverse('profile-index', kwargs={'id': 1}),

        )
        self.assertEqual(response.status_code, 302)

    def test_profile_update_not_loggued_in(self):
        response = self.c.post(
            reverse('profile-update', kwargs={'id': 1})

        )
        self.assertEqual(response.status_code, 302)
