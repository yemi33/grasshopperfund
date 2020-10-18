from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Profile


class TestLogin(TestCase):
    def setUp(self):
        self.username = "test"
        self.email = "test@email.com"
        self.password = "testing#2020"
        User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
            )

    def tearDown(self):
        # cascade will delete Profile too
        User.objects.get(username=self.username).delete()


    def test_login_required(self):
        response = self.client.get(reverse('profile'))
        print(response)
