from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TestSetup(APITestCase):
    def setUp(self):
        self.user_profile = reverse('userprofile')

        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.data={
            "picture": open("test_images/profile.jpg", "rb"),            
            "name": "test",
            "email":"test@12.com",
            "bio":"hello"
        }
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
