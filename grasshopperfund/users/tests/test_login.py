from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth


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


    def test_bad_login(self):
        response = self.client.post(
            reverse('login'),
            data = {
                'username': "lololol",
                'password': "incorrect",
            }
        )
        # check if user is authenticated
        user = auth.get_user(self.client)
        assert not user.is_authenticated

        response = self.client.get(reverse('delete-profile'))
        assert response.status_code == 302
        response = self.client.get(reverse('update-profile'))
        assert response.status_code == 302

    def test_login(self):
        response = self.client.post(
            reverse('login'),
            data = {
                'username': self.username,
                'password': self.password,
            }
        )

        # check if user is authenticated
        user = auth.get_user(self.client)
        assert user.is_authenticated

        response = self.client.get(reverse('update-profile'))
        assert response.status_code == 200
        response = self.client.get(reverse('delete-profile'))
        assert response.status_code == 200
        self.client.logout()


    def test_logout(self):
        self.client.login(
            username = self.username, 
            password = self.password
        )
        
        
        response = self.client.get(
            reverse('logout')
        )

        # check if user is authenticated
        user = auth.get_user(self.client)
        assert not user.is_authenticated

