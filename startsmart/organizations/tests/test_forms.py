from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Organization, Post
from ..forms import OrganizationForm
from .utils import BaseTestOrganizations



class TestForms(BaseTestOrganizations):

    def test_create_organization(self):
        self.client.login(username = self.username, password=self.password)

        response = self.client.get(reverse(
            "create-organization",
        ))

        # ensure that view has the form
        assert isinstance(response.context["form"], OrganizationForm)

        # New organization arguments


        self.new_org_owner = self.owner
        self.new_org_name = "NewOrg"
        self.new_org_description = "So the mollusk said to the sea cucumber..."

        # upload org image


        with open("./static/images/campaign_default_pic.png", 'rb') as image:
            self.new_org_image = SimpleUploadedFile(
                "campaign_default_pic.png",
                image.read(),
                content_type = "image/png"
            )

            response = self.client.post(
                reverse(
                    "create-organization",
                ),
                data = {
                    "owner": self.new_org_owner.id,
                    "name": self.new_org_name,
                    "description": self.new_org_description,
                    "image": self.new_org_image,
                },
            )

            # Succesfull form submit will redirect to view-org
            assert response.status_code == 302

        # verify that org was created
        organization = Organization.objects.get(name = self.new_org_name)
        assert self.new_org_description == organization.description
