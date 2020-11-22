from django.urls import reverse

from ..models import Post
from .utils import BaseTestPosts


class TestCreatePost(BaseTestPosts):

    def test_login_required(self):
        '''
        Verify that we can view a post
        '''

        response = self.client.get(reverse(
            "create-post",
            kwargs = {
                "organization_name": self.organization_name,
            }
        ))

        # assert redirect
        assert response.status_code == 302

    def test_login(self):
        self.client.login(
            username = self.username,
            password = self.password
        )

        response = self.client.get(reverse(
            "create-post",
            kwargs = {
                "organization_name": self.organization_name,
            }
        ))

        # assert redirect
        assert response.status_code == 200

        self.client.logout()


    def test_create_post(self):
        '''
        test updating existing post
        '''
        self.client.login(
            username = self.username,
            password = self.password
        )
        new_text = "new post wassup"
        response = self.client.post(
            reverse(
                "create-post",
                kwargs = {
                    "organization_name": self.organization_name,
                }
            ),
            data = {
                "author": self.owner.id,
                "organization": self.organization.id,
                "text": new_text
            }
        )
        # assert redirect to view-post
        assert response.status_code == 302

        # check that post text has been created
        new_post = Post.objects.get(text = new_text)
