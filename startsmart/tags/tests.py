from django.test import TestCase
from startsmart.campaigns.models import Campaign
from startsmart.tags.models import Tags
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.campaign_list = self._create_lists_of_campaign_for_tag()
        self.tag_list = self._create_tag()

    def tearDown(self) -> None:
        del self.campaign_list
        self.tag_list.campaign.clear()

    def _create_lists_of_campaign_for_tag(self):
        self.creator = User.objects.create_user(username='randomdude', email='random@email.com',
                                                password='randomdudeiscool70')
        self.title = 'Jazz festival'
        self.description = 'Come join us for smooth jazz festival'
        self.targetmoney = 89
        self.currentmoney = 10
        self.daysleft = 10
        self.num_of_backers = 20

        campaign1 = Campaign.objects.create(creator=self.creator, title=self.title,
                                                description=self.description, target_money=self.targetmoney,
                                                days_left=self.daysleft)
        self.creator = User.objects.create_user(username='testeruser12', email='testeruser12@email.com',
                                                password='testerishere800')
        self.title = 'Smooth jazz concert'
        self.description = 'This event will be held at the sea'
        self.targetmoney = 70
        self.currentmoney = 5
        self.daysleft = 50
        self.num_of_backers = 15

        campaign2 = Campaign.objects.create(creator=self.creator, title=self.title,
                                            description=self.description, target_money=self.targetmoney,
                                            days_left=self.daysleft)

        campaign1.save()
        campaign2.save()

        campaigns_list = [campaign1, campaign2]

        return campaigns_list

    def _create_tag(self):
        tag = Tags(name='jazz')
        tag.save()
        for campaign_num in self.campaign_list:
            tag.campaign.add(campaign_num)
        return tag

    def test_tag_created(self):
        self.assertEqual(len(Tags.objects.get(name=self.tag_list.name).campaign.all()), 2)
        pass


