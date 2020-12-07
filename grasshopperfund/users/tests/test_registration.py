from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from ...tags.models import Tag
from ..models import Profile


class TestRegistration(TestCase):
    def setUp(self):
        self.username = "new_user"
        self.password = "newnewnew1234"
        self.email = "new_user@grasshopperfund.com"

        self.tag_names = [
            "test",
            "advertising",
            "gaming"
        ]
        self.tags = self._create_tags(self.tag_names)

        # a quick reference to a tag
        self.tag = self.tags[0]


    def _create_tags(self, tag_names: list) -> list:
        '''
        Create tags from a list of tag names
        '''
        tags = []
        for name in tag_names:
            tag = Tag.objects.create(
                name=name
            )
            tags.append(tag)

        return tags

    def test_registration(self):
        '''
        Test creating a new user
        '''
        response = self.client.post(
            reverse('register'),
            data = {
                'username': self.username,
                'password1': self.password,
                'password2': self.password,
                'email': self.email,
            }
        )

        # assert redirect after successful registration
        assert response.status_code == 302

        # verify new user created
        assert Profile.objects.filter(user__username = self.username).exists()

        # now select interested tags
        response = self.client.post(
            reverse('add-interested-tags'),
            data = {
                'interested_tags': {
                    self.tag.id
                }
            }
        )

        # assert redirect after successful selection
        assert response.status_code == 302

        # check that interested tag has been added
        assert Profile.objects.get(
            user__username=self.username
            ).interested_tags.filter(
                name=self.tag.name
                ).exists()







