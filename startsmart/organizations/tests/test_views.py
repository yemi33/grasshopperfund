import random

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Organization, Post

class TestModels(TestCase):
    def setUp(self):
        '''
        Must follow this order
        '''
        self.owner = self._create_organization_owner()
        self.organization = self._create_organization()
        self.owner_posts = self._create_posts_from_owner()

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
            posts.append(posts)

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

    def test_view_organization(self):
        '''
        Verify that we can view our org
        '''
        response = self.client.get(reverse(
            "view-organization",
            kwargs = {
                "organization_name": self.organization_name
            }
        ))

        assert response.status_code == 200

        organization = response.context['organization']

        assert self.organization_name == organization.name

    def test_delete_organization(self):
        '''
        Verify that we can delete our org
        '''
        self.client.login(username = self.username, password=self.password)

        response = self.client.post(reverse(
            "delete-organization",
            kwargs = {
                "organization_name": self.organization_name
            }
        ))


        # successful delete redirects user to home
        assert response.status_code == 302

        # check that organization does not exist
        self.assertRaises(
            Organization.DoesNotExist,
            Organization.objects.get,
            name = self.organization_name,
        )

        self.client.logout()


    def test_does_not_exist(self):
        '''
        Verify behavior for when an organization doesn't exist
        '''
        # get organization that doesn't exist
        response = self.client.get(reverse(
            "view-organization",
            kwargs = {
                "organization_name": "skeet on the beet"
            }
        ))
        assert response.status_code == 404

        self.client.login(username = self.username, password=self.password)

        response = self.client.get(reverse(
            "update-organization",
            kwargs = {
                "organization_name": "skeet on the beet"
            }
        ))
        # 404 error if organization doesn't exist
        assert response.status_code == 404

        response = self.client.get(reverse(
            "delete-organization",
            kwargs = {
                "organization_name": "skeet on the beet"
            }
        ))
        assert response.status_code == 404

        self.client.logout()



    def test_browse_organizations(self):
        '''
        Verify that our org is on the browse page
        '''
        response = self.client.get(reverse("browse-organizations"))

        assert response.status_code == 200

        organizations = response.context['organizations']

        org_exists = False

        for organization in organizations:
            if organization.name == self.organization_name:
                org_exists = True
                break

        assert org_exists
