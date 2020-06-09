from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post


# Create your tests here.
class ViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test', password='test')
        Post.objects.create(title='slug', content='content', user=user)

    c = Client()

    def test_post_list_uri(self):
        response = self.c.get(
            reverse('post_list')
        )
        self.assertEqual(response.status_code, 200)

    def test_most_popular_uri(self):
        response = self.c.get(
            reverse('post_popular')
        )
        self.assertEqual(response.status_code, 200)

    def test_detail_uri(self):
        response = self.c.get(
            reverse('post_detail', kwargs={'slug': 'slug'})
        )
        self.assertEqual(response.status_code, 200)
