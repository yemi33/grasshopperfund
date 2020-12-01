from django.test import TestCase
from django.contrib.auth.models import User

from ...tags.models import Tags
from ..models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.profile = self._create_profile()

        self.tag_names = [
            "test",
            "advertising",
            "gaming"
        ]
        self.tags = self._create_tags(self.tag_names)

        # a quick reference to a tag
        self.tag = self.tags[0]


    def _create_profile(self) -> Profile:
        self.username = "test"
        self.email = "test@email.com"
        self.password = "testing#2020"
        self.user = User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
        )
        return Profile.objects.get(user__username = self.username)


    def _create_tags(self, tag_names: list) -> list:
        '''
        Create tags from a list of tag names
        '''
        tags = []
        for name in tag_names:
            tag = Tags.objects.create(
                name=name
            )
            tags.append(tag)

        return tags


    def test_add_interested_tag(self):
        '''
        Test adding an interested tag to a user
        '''
        self.profile.interested_tags.add(self.tag)

        assert self.profile.interested_tags is not None
        assert self.profile.interested_tags.filter(name=self.tag.name).exists()
        assert self.tag.interested_users.filter(user__username=self.username).exists()



    def tearDown(self):
        # cascade will delete Profile too
        User.objects.get(username=self.username).delete()
