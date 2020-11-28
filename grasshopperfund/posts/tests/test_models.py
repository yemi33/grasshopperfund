from .utils import BaseTestPosts



class TestModels(BaseTestPosts):

    def test_liked(self):

        assert self.post.already_liked(self.liker) == True


    def test_like_post(self):

        # since the post is already liked, post should be unliked
        self.post.like(self.liker)
        assert self.post.already_liked(self.liker) == False

        # now add a like by liking again
        self.post.like(self.liker)
        assert self.post.already_liked(self.liker) == True
