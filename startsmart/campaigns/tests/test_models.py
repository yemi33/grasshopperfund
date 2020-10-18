import random

from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Campaign, Donation

class TestModels(TestCase):
    def setUp(self):
        '''
        Must follow this order
        '''
        self.creator = self._create_campaign_creator()
        self.campaign = self._create_campaign()
        self.donors = self._create_donors()
        self.donations = self._create_donations()


    def _create_campaign_creator(self):
        self.username = "testing"
        self.email = "test@email.com"
        self.password = "testing#2020"

        creator = User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
        )

        return creator

    def _create_campaign(self):
        '''
        Create test campaign
        '''

        self.title = "test campaign"
        self.description = "for testing"
        self.target_money = 100
        self.current_money = 0
        self.days_left = 100
        self.num_of_backers = 100

        campaign = Campaign.objects.create(
            creator = self.creator,
            title = self.title,
            description=self.description,
            target_money = self.target_money,
            days_left = self.days_left
        )

        assert len(campaign.backers) == 0
        assert len(campaign.donations.all()) == 0

        return campaign

    def _create_donors(self, amount = 5) -> list:
        '''
        Create a list of unique donors
        '''
        self.donor_username = "donor"
        self.donor_email = "donor@email.com"

        donors = list()
        username = self.donor_username
        email = self.donor_email

        for i in range(amount):
            donor = User.objects.create_user(
                username = username,
                password = self.password,
                email=email
            )
            donors.append(donor)
            username += 'a'
            email = 'a' + email

        return donors

    def _create_donations(self, amount = 5) -> list:
        '''
        Create donations from previously made donors to
        the previously made campaign
        '''
        donations = list()

        for i in range(amount):
            donation_amount = random.randrange(1,10)
            donation = Donation.objects.create(
                campaign = self.campaign,
                amount = donation_amount,
                donor = random.choice(self.donors)
            )
            donations.append(donation)

        return donations

    def tearDown(self):
        '''
        Delete all objects created
        '''
        for donation in self.donations:
            donation.delete()

        for donor in self.donors:
            donor.delete()

        self.campaign.delete()
        self.creator.delete()


    def test_campaign_created(self):
        campaign = Campaign.objects.get(
            creator__username = self.username,
            title = self.title
        )

        self.assertEqual(campaign.description, self.description)


    def test_donations_made(self):
        donations = list(self.campaign.donations.all())

        assert len(self.campaign.backers) > 0
        assert len(self.donations) == len(donations)
