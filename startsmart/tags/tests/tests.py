from django.test import TestCase
from startsmart.campaigns.models import Campaign
from startsmart.tags.models import Tags
from django.contrib.auth.models import User


from ...organizations.models import Organization

# Create your tests here.
class TestModels(TestCase): 
    def setUp(self):
        print("From test tags")
        self.owner = self._create_organization_owner()
        self.organization = self._create_organization()
        self.campaign_list = self._create_lists_of_campaign_for_tag()
        self.tag_list = self._create_tag()


    def tearDown(self) -> None:
        del self.campaign_list
        self.tag_list.campaigns.clear()

    def _create_organization_owner(self):
        '''
        Create the User that will own the organization.
        Save the attributes so we can test that the user exists
        '''
        self.username = "testing"
        self.email = "test@email.com"
        self.password = "testing#2020"

        owner = User.objects.create_user(
            username = self.username,
            password = self.password,
            email=self.email
        )

        return owner



    def _create_organization(self):
        '''
        Create an organization.
        Save the attributes to test that the organization exists
        '''
        self.organization_name = "Test Org Inc."
        self.organization_description = "for testing"

        organization = Organization.objects.create(
            owner = self.owner,
            name = self.organization_name,
            description = self.organization_description,
        )


        return organization

    def _create_lists_of_campaign_for_tag(self):
        self.creator = self.owner
        self.title = 'Jazz festival'
        self.description = 'Come join us for smooth jazz festival'
        self.targetmoney = 89
        self.currentmoney = 10
        self.daysleft = 10
        self.num_of_backers = 20

        campaign1 = Campaign.objects.create(creator=self.creator, title=self.title,
                                                organization = self.organization,
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

        campaign2 = Campaign.objects.create(creator=self.creator, title=self.title, organization = self.organization,
                                            description=self.description, target_money=self.targetmoney,
                                            days_left=self.daysleft)

        campaign1.save()
        campaign2.save()

        campaigns_list = [campaign1, campaign2]

        return campaigns_list

    def _create_tag(self):
        print("X")
        tag = Tags(name='jazz')
        tag.save()
        for campaign_num in self.campaign_list:
            tag.campaigns.add(campaign_num)
        return tag

    def test_tag_created(self):
        print("test tag created starting")
        self.assertEqual(len(Tags.objects.get(name=self.tag_list.name).campaigns.all()), 2)
        pass
