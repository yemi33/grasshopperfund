import random

from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Organization

class TestModels(TestCase):
    def setUp(self):
        '''
        Must follow this order
        '''
        self.owner = self._create_organization_owner()
        self.organization = self._create_organization()

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

    def test_organization_created(self):
        '''
        Verify that setUp created an organization
        '''

        # Query for the org
        organization = Organization.objects.get(
            name = self.organization_name,
        )

        # Check that this org is the org we just made

        self.assertEqual(
            organization.description,
            self.organization_description
        )
