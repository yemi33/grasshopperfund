from django.urls import reverse


from ...posts.models import Post
from ..models import Organization
from .utils import BaseTestOrganizations


class TestViews(BaseTestOrganizations):

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

        response = self.client.get(reverse(
            "delete-organization",
            kwargs = {
                "organization_name": self.organization_name
            }
        ))

        # verify that the organization to be deleted is the organization
        # we just made
        organization = response.context['organization']
        assert self.organization_name == organization.name



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

        # make org again
        self.organization = self._create_organization()
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
