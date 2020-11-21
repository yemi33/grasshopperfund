from django.urls import reverse

from ..models import Post
from .utils import BaseTestPosts


class TestDeletePost(BaseTestPosts):



    def _test_login_required(self):
        '''
        Verify that we can view a post
        '''

        response = self.client.get(reverse(
            "delete-post",
            kwargs = {
                "organization_name": self.organization_name,
                "post_id": self.post.id,
            }
        ))

        # assert redirect
        assert response.status_code == 302

    def _test_login(self):
        self.client.login(
            username = self.username,
            password = self.password
        )

        response = self.client.get(reverse(
            "delete-post",
            kwargs = {
                "organization_name": self.organization_name,
                "post_id": self.post.id,
            }
        ))

        # assert redirect
        assert response.status_code == 200

        self.client.logout()


    def test_delete_post(self):
        '''
        test updating existing post
        '''

        # run previous tests first
        self._test_login_required()
        self._test_login()

        self.client.login(
            username = self.username,
            password = self.password
        )
        response = self.client.post(
            reverse(
                "delete-post",
                kwargs = {
                    "organization_name": self.organization_name,
                    "post_id": self.post.id,
                }
            )
        )
        # assert redirect to view-organization
        assert response.status_code == 302

        # check that post is gone
        self.assertRaises(
            Post.DoesNotExist,
            Post.objects.get,
            pk = self.post.id,
        )
