from django.test import TestCase
from django.urls import reverse

from ..tests.test_search_campaigns import TestModels
from ..models import Campaign
from ...tags.models import Tag

class MyTestCase(TestModels):
    def setUp(self) -> None:
        TestModels.setUp(self)

    def test_search_for_campaigns_existed(self):
        x = self.client.get('%s?search_query=jaz+music' % reverse('search-campaign'))
        self.assertEqual(len(x.context['campaigns']), 1)

    def test_search_for_multiple_campaigns1(self):
        x = self.client.get('%s?search_query=jaz+rock' % reverse('search-campaign'))
        self.assertEqual(len(x.context['campaigns']), 2)

    def test_number_of_no_campaigns(self):
        x = self.client.get('%s?search_query=music+movie' % reverse('search-campaign'))
        self.assertEqual(len(x.context['campaigns']), len(Campaign.objects.all()))

    def test_search_for_campaigns_for_pagination(self):
        tag = Tag.objects.filter(name='rock')
        campaigns_list1 = [{'creator': self.owner, 'title': 'Movie rock festival',
                            'description': 'Come join us for movie festival',
                            'target_money': 95, 'days_left': 30},
                           {'creator': self.owner, 'title': 'Rock and Drive',
                            'description': 'driving fun',
                            'target_money': 75, 'days_left': 27},
                           {'creator': self.owner, 'title': 'Rock at the park',
                            'description': 'Come join us for a good outdoor nighttime',
                            'target_money': 81, 'days_left': 14}]
        for campaign_info in campaigns_list1:
            campaign1 = Campaign.objects.create(creator=campaign_info['creator'], title=campaign_info['title'],
                                                    organization = self.organization,
                                                    description=campaign_info['description'],
                                                target_money=campaign_info['target_money'],
                                                    days_left=campaign_info['days_left'])
            campaign1.save()
            campaign1.tags.add(tag[0])
            tag[0].campaigns.add(campaign1)
        x = self.client.get('%s?search_query=' % reverse('search-campaign'))
        self.assertEqual(str(x.context['page_res']), '<Page 1 of 2>')
        x = self.client.get('%s?search_query=rock' % reverse('search-campaign'))
        self.assertEqual(str(x.context['page_res']), '<Page 1 of 1>')

    def test_search_for_campaigns_show_results(self):
        tag = Tag.objects.filter(name='rock')
        campaigns_list1 = [{'creator': self.owner, 'title': 'Movie rock festival',
                            'description': 'Come join us for movie festival',
                            'target_money': 95, 'days_left': 30},
                           {'creator': self.owner, 'title': 'Rock and Drive',
                            'description': 'driving fun',
                            'target_money': 75, 'days_left': 27},
                           {'creator': self.owner, 'title': 'Rock at the park',
                            'description': 'Come join us for a good outdoor nighttime',
                            'target_money': 81, 'days_left': 14}]
        for campaign_info in campaigns_list1:
            campaign1 = Campaign.objects.create(creator=campaign_info['creator'], title=campaign_info['title'],
                                                organization=self.organization,
                                                description=campaign_info['description'],
                                                target_money=campaign_info['target_money'],
                                                days_left=campaign_info['days_left'])
            campaign1.save()
            campaign1.tags.add(tag[0])
            tag[0].campaigns.add(campaign1)
        x = self.client.get('%s?search_query=rock' % reverse('search-campaign'))
        self.assertEqual(x.context['number_of_campaigns'], 4)

    def test_status_code_for_search_campaigns(self):
        x = self.client.get('%s?search_query=rock' % reverse('search-campaign'))
        self.assertEqual(x.status_code, 200)

    def test_status_code_for_search_campaigns_with_no_404(self):
        x = self.client.get('%s?search_query=rock' % reverse('search-campaign'))
        self.assertNotEqual(x.status_code, 404)
