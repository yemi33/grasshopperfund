from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Campaign

class TestModels(TestCase):
    def setUp(self):
        self.username = "test"
        self.email = "test@email.com"
        self.password = "testing#2020"

        self.creator = User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
        )
        self.title = "test campaign"
        self.description = "for testing"
        self.target_money = 100
        self.current_money = 0
        self.days_left = 100
        self.num_of_backers = 100

        self.campaign = Campaign.objects.create(
            creator = self.creator,
            title = self.title,
            description=self.description,
            target_money = self.target_money,
            days_left = self.days_left
        )



    def tearDown(self):
        # cascade will delete Profile too
        User.objects.get(username=self.username).delete()
        Campaign.objects.all().delete()


    def test_campaign_created(self):
        campaign = Campaign.objects.get(
            creator__username = self.username,
            title = self.title
        )

        self.assertEqual(campaign.description, self.description)
