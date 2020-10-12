from django.db import models


class Campaign(models.Model):
    user = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    target_money = models.IntegerField()
    current_money = models.IntegerField()
    days_left = models.IntegerField()
    num_of_backers = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        unique_together = (('user','title'),)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
