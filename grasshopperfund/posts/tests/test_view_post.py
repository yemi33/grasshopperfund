from django.urls import reverse

from .utils import BaseTestPosts


class TestViewPost(BaseTestPosts):

    def test_view(self):
        '''
        Verify that we can view a post
        '''

        response = self.client.get(reverse(
            "view-post",
            kwargs = {
                "organization_name": self.organization_name,
                "post_id": self.post.id,
            }
        ))

        assert response.status_code == 200

        post = response.context['post']

        self.assertEqual(post, self.post)
