'''
utilities for post test
'''

from django.test import TestCase
from django.contrib.auth.models import User

from ...organizations.models import Organization
from ..models import Post



'''
Utility classes for testing
'''

from django.test import TestCase
from django.contrib.auth.models import User

from ...posts.models import Post
from ..models import Organization

class BaseTestPosts(TestCase):
    def setUp(self):
        '''
        Must follow this order
        '''
        self.owner = self._create_organization_owner()

        # posts author is also org owner
        self.author = self.owner

        self.organization = self._create_organization()
        self.posts = self._create_posts_from_owner()

        # default post to check is the first in self.posts
        self.post = self.posts[0]


        # set user which likes posts
        self.liker = self.owner

        # like posts
        self.likes = self._like_posts(self.posts,self.liker)


    def tearDown(self):
        '''
        Delete all objects created
        '''

        self.owner.delete()

    def _create_organization_owner(self):
        '''
        Create the User that will own the organization.
        Save the attributes so we can test that the user exists
        '''
        self.username = "testing"
        self.email = "test@email.com"
        self.password = "testing#2020"

        owner = User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
        )

        return owner



    def _create_posts_from_owner(self):
        '''
        Create posts within the test organization authored by the owner
        '''
        self.post_texts = [
            "Hello world",
            "This is a test post",
        ]

        posts = []

        for text in self.post_texts:
            post = Post.objects.create(
                author = self.owner,
                organization = self.organization,
                text = text,
            )
            posts.append(post)

        return posts

    def _create_organization(self):
        '''
        Create an organization.
        Save the attributes to test that the organization exists
        '''
        self.organization_name = "Test Org Inc."
        self.organization_description = "for testing"

        organization = Organization.objects.create(
            owner = self.owner,
            name = self.organization_name,
            description = self.organization_description,
        )


        return organization

    def _like_posts(self, posts: list, liker: User):
        '''
        Like posts in list
        '''
        likes = []
        for post in posts:
            likes.append(post.add_like(liker))

        return likes
