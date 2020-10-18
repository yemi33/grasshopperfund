from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Profile


class TestProfile(TestCase):
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


    def test_profile_created(self):
        test_user = Profile.objects.get(user__username = self.username)

        self.assertEqual(test_user.user.username, self.username)
        self.assertEqual(test_user.email, self.email)
