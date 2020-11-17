from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Organization, Post
from ..forms import OrganizationForm
from .utils import BaseTestOrganizations



class TestUpdateOrganization(BaseTestOrganizations):

    def test_form(self):
        self.client.login(username = self.username, password=self.password)

        response = self.client.get(reverse(
            "update-organization",
            kwargs = {
                "organization_name": self.organization_name
            }
        ))

        # ensure that view has the form
        assert isinstance(response.context["form"], OrganizationForm)

        # New organization arguments


        self.updated_org_owner = self.owner
        self.updated_org_name = "UpdatedOrg"
        self.updated_org_description = "So the mollusk said to the sea cucumber..."

        # upload org image


        with open("./static/images/campaign_default_pic.png", 'rb') as image:
            self.updated_org_image = SimpleUploadedFile(
                "campaign_default_pic.png",
                image.read(),
                content_type = "image/png"
            )

            response = self.client.post(
                reverse(
                    "update-organization",
                    kwargs = {
                        "organization_name": self.organization_name
                    }
                ),
                data = {
                    "owner": self.updated_org_owner.id,
                    "name": self.updated_org_name,
                    "description": self.updated_org_description,
                    "image": self.updated_org_image,
                },
            )

            # Succesfull form submit will redirect to view-org
            assert response.status_code == 302

        # verify that org was created
        organization = Organization.objects.get(name = self.updated_org_name)
        assert self.updated_org_description == organization.description


    
