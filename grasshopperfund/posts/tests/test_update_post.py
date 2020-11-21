from django.urls import reverse

from ..models import Post
from .utils import BaseTestPosts


class TestUpdatePost(BaseTestPosts):



    def test_login_required(self):
        '''
        Verify that we can view a post
        '''

        response = self.client.get(reverse(
            "update-post",
            kwargs = {
                "organization_name": self.organization_name,
                "post_id": self.post.id,
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
            "update-post",
            kwargs = {
                "organization_name": self.organization_name,
                "post_id": self.post.id,
            }
        ))

        # assert redirect
        assert response.status_code == 200

        self.client.logout()


    def test_update_post(self):
        '''
        test updating existing post
        '''
        self.client.login(
            username = self.username,
            password = self.password
        )
        new_text = "wasssupppppp this is neeewwww"
        response = self.client.post(
            reverse(
                "update-post",
                kwargs = {
                    "organization_name": self.organization_name,
                    "post_id": self.post.id,
                }
            ),
            data = {
                "text": new_text
            }
        )
        # assert redirect to view-post
        assert response.status_code == 302

        # check that post text has changed
        updated_post = Post.objects.get(pk = self.post.id)
        self.assertEqual(updated_post.text, new_text)
