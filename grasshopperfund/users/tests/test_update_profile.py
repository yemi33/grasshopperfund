from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile


from ..models import Profile


class TestUpdateProfile(TestCase):
    def setUp(self):
        self.username = "test"
        self.email = "test@email.com"
        self.password = "testing#2020"
        self.user = User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
            )



    def test_update_profile(self):
        self.client.login(
            username = self.username, 
            password = self.password
        )

        # currently, only email can be updated
        updated_username = "updated_username"
        updated_password = "updated"
        updated_email = "updated_email@grasshoppfund.com"

        # need to open image for the updated profile
        with open("./static/images/default.jpg", 'rb') as image:
            updated_profile_image = SimpleUploadedFile(
                "default.jpg",
                image.read(),
                content_type = "image/jpg"
            )

            response = self.client.post(
                reverse(
                    "update-profile",
                ),
                data = {
                    'user': self.user.id,
                    "email": updated_email,
                    "image": updated_profile_image,
                },
            )

            # Succesfull form submit will redirect to view-profile
            assert response.status_code == 302

        # check that profile has been changed
        assert Profile.objects.filter(email=updated_email).exists()

        # delete profile
        response = self.client.post(
            reverse('delete-profile'),
        )

        assert not Profile.objects.filter(email=updated_email).exists()

        self.client.logout()
