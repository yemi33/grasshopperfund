from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


from ...posts.models import Post
from ...posts.forms import PostForm
from ..models import Organization
from .utils import BaseTestOrganizations



class TestCreatePost(BaseTestOrganizations):

    def test_create_post(self):
        self.client.login(username = self.username, password=self.password)

        response = self.client.get(reverse(
            "view-organization",
            kwargs = {
                "organization_name": self.organization_name
            }
        ))

        # ensure that view has the form
        assert isinstance(response.context["form"], PostForm)

        new_text = "new post in organization this is."
        response = self.client.post(
            reverse(
                "view-organization",
                kwargs = {
                    "organization_name": self.organization_name
                }
            ),
            data = {
                "author": self.owner.id,
                "text": new_text
            }
        )

        # Succesfull form submit will redirect to view-org
        assert response.status_code == 302

        # verify that post was created
        new_post = Post.objects.get(text = new_text)

        self.client.logout()
