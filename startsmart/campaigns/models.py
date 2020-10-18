from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    target_money = models.IntegerField()
    days_left = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='campaign_pics')

    search_fields = ['creator__username']

    class Meta:
        unique_together = (('creator','title'),)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def current_money(self) -> Decimal:
        '''
        get current money from sum of donation amounts
        '''
        money = Decimal(0)
        for donation in self.donations.all():
            money += 0
        return money

    @property
    def num_of_donations(self) -> list:
        return len(list(self.donations.all()))


    @property
    def backers(self) -> list:
        '''
        get backers from unique donors
        '''
        backers = set()
        for donation in self.donations.all():
            backers.add(donation.donor)

        return backers

    @property
    def num_of_backers(self) -> int:
        '''
        get num_of_backers from len of backers
        '''
        return len(self.backers)

class Donation(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name='donations')
    amount = models.DecimalField(decimal_places=2, max_digits=7)
    donor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='donations', null=True)
    date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"To {self.campaign.title} | from {self.donor.username} | amount: {self.amount} | {self.date}"
