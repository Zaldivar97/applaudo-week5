from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class ViewTest(TestCase):
    c = Client()

    def test_postlist_uri(self):
        response = self.c.get(
            reverse('post_list')
            )
        self.assertEqual(response.status_code, 200)
    
    def test_mostpopular_uri(self):
        response = self.c.get(
            reverse('post_popular')
        )
        self.assertEqual(response.status_code, 200)
    
    def test_detail_uri(self):
        response = self.c.get(
        reverse('post_detail', kwsargs={'slug':'slug'})
        )
        self.assertEqual(response.status_code, 200)
