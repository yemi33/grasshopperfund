from django.test import TestCase
from ..models import Campaign
from ...tags.models import Tag
from ...organizations.models import Organization
from django.contrib.auth.models import User
import re

from django.db.models import Q

class TestModels(TestCase):
    def setUp(self) -> None:
        '''Setting up for searching campaigns feature'''
        self.owner = self._create_organization_owner()
        self.organization = self._create_organization()
        self.campaign_list = self._create_lists_of_campaign_for_tag()

    def _create_organization_owner(self):
        '''
        Create the User that will own the organization.
        Save the attributes so we can test that the user exists
        '''
        self.username = "testing"
        self.email = "test@email.com"
        self.password = "testing#2020"

        owner = User.objects.create_user(
            username=self.username,
            password=self.password,
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
        '''
        Creates a list of campaigns (note that default is two campaigns) for testing the tags
        '''
        campaigns_list1 = [{'creator':self.owner, 'title':'Jazz festival',
                            'description': 'Come join us for smooth jazz festival',
                            'target_money' : 89, 'days_left': 10},
                           {'creator': self.owner, 'title': 'Rock concert tribute to Queens',
                            'description': 'A tribute to Queens',
                            'target_money': 80, 'days_left': 20}, {'creator':self.owner, 'title':'Raise for running awarness',
                            'description': 'Come join us for a good run of running',
                            'target_money' : 70, 'days_left': 12} ]
        campaigns_list_result = []
        tags_names_list = ['jazz', 'rock', 'excercise']
        for tag_name, campaign_info in zip(tags_names_list, campaigns_list1):
            campaign1 = Campaign.objects.create(creator=campaign_info['creator'], title=campaign_info['title'],
                                                    organization = self.organization,
                                                    description=campaign_info['description'],
                                                target_money=campaign_info['target_money'],
                                                    days_left=campaign_info['days_left'])
            campaign1.save()
            tag = Tag(name=tag_name)
            tag.save()
            campaign1.tags.add(tag)
            tag.campaigns.add(campaign1)
            campaigns_list_result.append(campaign1)

        # campaign1 = Campaign.objects.create(creator=self.creator, title=self.title,
        #                                         organization = self.organization,
        #                                         description=self.description, target_money=self.targetmoney,
        #                                         days_left=self.daysleft)
        # self.creator = User.objects.create_user(username='testeruser12', email='testeruser12@email.com',
        #                                         password='testerishere800')
        return campaigns_list_result

    def test_number_of_campaigns(self):
        '''Testing for a number of campaigns'''
        self.assertEqual(len(self.campaign_list), 3)

    def test_check_for_tags_in_campaigns(self):
        '''Testing for particular tags that have existed in one or more Campaigns'''
        tags_names_list = ['jazz', 'rock', 'excercise']
        count_i = 0
        self.assertEqual(self.campaign_list[0].tags.filter(name=tags_names_list[0]).exists(), True)
        for tag_name, campaign in zip(tags_names_list, self.campaign_list):
            if campaign.tags.filter(name=tag_name).exists(): count_i += 1
        self.assertEqual(count_i, 3)

        assert len(self.campaign_list[0].all_tags) > 0

    def test_search_for_campaigns_1(self):
        '''Testing a search on campaign that contains the keyword jazz'''
        self.assertEqual(str(Campaign.objects.filter(title__icontains='jazz')[0]), 'Jazz festival')

    def test_search_for_campaigns_2(self):
        '''Testing a search on campaign that contains the keyword run'''
        self.assertEqual(str(Campaign.objects.filter(title__icontains='run')[0]), 'Raise for running awarness')

    def test_search_for_campaigns_3(self):
        '''Testing a search on campaign that contains the keyword rock'''
        self.assertEqual(str(Campaign.objects.filter(title__icontains='rock')[0]), 'Rock concert tribute to Queens')

    def test_search_for_multiple_campaigns(self):
        '''Testing a search on multiple campaigns'''
        the_creator = self.owner
        the_title = 'Metallica rock tribute'
        the_organization = self.organization
        the_description = 'Join us for a night of Metallica'
        the_target_money = 59
        the_days_left = 97
        campaign = Campaign.objects.create(creator=the_creator,
                                           title=the_title,
                                           organization = the_organization,
                                           description=the_description,
                                           target_money=the_target_money,
                                           days_left=the_days_left)
        campaign.save()
        tag = Tag.objects.filter(name='rock')
        print(tag[0])
        campaign.tags.add(tag[0])
        self.assertEqual(Campaign.objects.filter(title__icontains='rock').count(), 2)

    def test_search_for_campaigns_from_different_owners_and_organizations(self):
        '''Testing a search on campaigns from different owners and organizations'''
        the_username = "testerx"
        the_email = "testerxy@email.com"
        the_password = "loliscool890"

        owner = User.objects.create_user(
            username=the_username,
            password=the_password,
            email=the_email
        )
        owner.save()
        the_organization_name = "Test Org XYZ."
        the_organization_description = "XYZ for testing purposes"

        organization = Organization.objects.create(
            owner=owner,
            name=the_organization_name,
            description=the_organization_description,
        )
        organization.save()
        the_creator = owner
        the_title = 'Old school jazz in cafe'
        the_organization = organization
        the_description = 'Join us for a night of old school jazz that is a tribute to the 1950s'
        the_target_money = 35
        the_days_left = 13
        campaign = Campaign.objects.create(creator=the_creator,
                                           title=the_title,
                                           organization=the_organization,
                                           description=the_description,
                                           target_money=the_target_money,
                                           days_left=the_days_left)
        campaign.save()
        tag = Tag.objects.filter(name='jazz')
        print(tag[0])
        campaign.tags.add(tag[0])
        testerx_exists = False
        self.assertEqual(Campaign.objects.filter(title__icontains='jazz').count(), 2)
        for campaign in Campaign.objects.all():
            if str(campaign.creator) == 'testerx': testerx_exists = True
        self.assertEqual(testerx_exists, True)

    def test_search_for_campaigns_from_search_bar(self):
        '''Testing a search on campaigns'''
        query_result = [res_word for res_word in re.split('[, ]', 'jaz,  rock  run,') if res_word != '']
        temp = Campaign.objects.none()
        for word in query_result:
            res = Campaign.objects.all().filter(Q(title__icontains=word))
            temp |= res
        self.assertEqual(len(temp), 3)

    def test_search_for_campaigns_from_the_search_bar_with_tags(self):
        '''Testing a search on campaign using tags and campaigns'''
        query_result = [res_word for res_word in re.split('[, ]', 'jaz,  rock  run,') if res_word != '']
        tag_temp = Tag(name='music')
        tag_temp.save()
        for word in query_result:
            campaign = Campaign.objects.get(title__icontains=word)
            campaign.save()
            campaign.tags.add(tag_temp)
            tag_temp.campaigns.add(campaign)
        res = Campaign.objects.filter( Q(tags__name__icontains='music') | Q(title__icontains='jazz'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        self.assertEqual(len(res1), 3)

    def test_search_for_campaigns_from_the_search_bar_with_no_existing_tags_or_campaigns(self):
        '''Testing a search on campaign using no existing tags or campaigns'''
        res = Campaign.objects.filter(Q(tags__name__icontains='stuff') | Q(title__icontains='disco'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        self.assertEqual(len(res1), 0)

    def test_search_for_campaigns_from_the_search_bar_with_existing_tags_and_campaigns(self):
        '''Testing a search on campaign using existing tags and campaigns'''
        res = Campaign.objects.filter(Q(tags__name__icontains='rock') | Q(title__icontains='jazz'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        self.assertEqual(len(res1), 2)

    def test_search_for_campaigns_from_the_search_bar_with_tags_mapping_to_campaigns(self):
        '''Testing a search on campaign using tags that are mapped to campaigns'''
        res = Campaign.objects.filter(Q(tags__name__icontains='jazz') | Q(title__icontains='jazz'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        self.assertEqual(len(res1), 1)

    def test_search_for_campaigns_from_the_search_bar_with_tags_mapping_to_multiple_campaigns(self):
        '''Testing a search on campaign using tags that are mapped to multiple campaigns'''
        the_username = "testerx"
        the_email = "testerxy@email.com"
        the_password = "loliscool890"

        owner = User.objects.create_user(
            username=the_username,
            password=the_password,
            email=the_email
        )
        owner.save()
        the_organization_name = "Test Org XYZ."
        the_organization_description = "XYZ for testing purposes"

        organization = Organization.objects.create(
            owner=owner,
            name=the_organization_name,
            description=the_organization_description,
        )
        organization.save()
        the_creator = owner
        the_title = 'Old school jazz in cafe'
        the_organization = organization
        the_description = 'Join us for a night of old school jazz that is a tribute to the 1950s'
        the_target_money = 35
        the_days_left = 13
        campaign = Campaign.objects.create(creator=the_creator,
                                           title=the_title,
                                           organization=the_organization,
                                           description=the_description,
                                           target_money=the_target_money,
                                           days_left=the_days_left)
        campaign.save()
        tag = Tag.objects.filter(name='jazz')
        campaign.tags.add(tag[0])
        tag[0].campaigns.add(campaign)
        res = Campaign.objects.filter(Q(tags__name__icontains='jazz') | Q(title__icontains='jazz'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        self.assertEqual(len(res1), 2)

    def test_search_for_campaigns_from_the_search_bar_with_tags_only(self):
        '''Testing a search on campaign using tags only'''
        the_username = "testerx"
        the_email = "testerxy@email.com"
        the_password = "loliscool890"

        owner = User.objects.create_user(
            username=the_username,
            password=the_password,
            email=the_email
        )
        owner.save()
        the_organization_name = "Test Org XYZ."
        the_organization_description = "XYZ for testing purposes"

        organization = Organization.objects.create(
            owner=owner,
            name=the_organization_name,
            description=the_organization_description,
        )
        organization.save()
        the_creator = owner
        the_title = 'Old school jazz in cafe'
        the_organization = organization
        the_description = 'Join us for a night of old school jazz that is a tribute to the 1950s'
        the_target_money = 35
        the_days_left = 13
        campaign = Campaign.objects.create(creator=the_creator,
                                           title=the_title,
                                           organization=the_organization,
                                           description=the_description,
                                           target_money=the_target_money,
                                           days_left=the_days_left)
        campaign.save()
        tag = Tag.objects.filter(name='jazz')
        campaign.tags.add(tag[0])
        tag[0].campaigns.add(campaign)
        res = Campaign.objects.filter(Q(tags__name__icontains='jazz') | Q(title__icontains='disco'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        self.assertEqual(len(res1), 2)

    def test_search_for_campaigns_from_the_search_bar_with_avoid_duplicate_campaigns(self):
        '''Testing a search on campaign in avoiding duplicating campaigns'''
        query_result = [res_word for res_word in re.split('[, ]', 'jaz,  rock  run,') if res_word != '']
        temp = Campaign.objects.none()
        tag_temp = Tag(name='music')
        tag_temp.save()
        for word in query_result:
            campaign = Campaign.objects.get(title__icontains=word)
            campaign.save()
            campaign.tags.add(tag_temp)
            tag_temp.campaigns.add(campaign)
        res = Campaign.objects.filter( Q(tags__name__icontains='music') | Q(title__icontains='jazz'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        temp |= res1
        res = Campaign.objects.filter(Q(tags__name__icontains='music') | Q(title__icontains='jazz'))
        res1 = Campaign.objects.filter(title__in=list(res.values_list('title', flat=True).distinct()))
        temp |= res1
        self.assertEqual(len(temp), 3)




