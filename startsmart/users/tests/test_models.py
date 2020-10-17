from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Profile





class TestProfile(TestCase):
    def setUp(self):
        self.username = "test"
        self.password = "testing#2020"
        User.objects.create_user(
            username = self.username,
            password = self.password
            )



    def test_profile_created(self):
        test_user = Profile.objects.get(user__username = self.username)

        self.assertEqual(test_user.user.username, self.username)
