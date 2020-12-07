from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=300, unique=True)
    # no need to indicate relationship with campaigns here. 
    # it is done in the "campaigns" app instead (campaigns/models.py)

    def __str__(self): return f"{self.name}"

    @property
    def all_campaigns(self):
        return self.campaigns.all()
