from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class ViewTest(TestCase):
    c = Client()

    def test_login(self):
        response = self.c.post(
            reverse('signup'),
            {'username':'name','password':'passw'}
            )
        print(response.__dict__)
        self.assertEqual(response.status_code, 200)
    
    def test_signup(self):
        response = self.c.post(
            reverse('signup'),
            {'username':'name','password':'passw'}
            )
        self.assertEqual(response.status_code, 200)
        
