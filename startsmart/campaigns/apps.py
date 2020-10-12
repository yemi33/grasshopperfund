from django.apps import AppConfig



print("YAAAA")
class CampaignsConfig(AppConfig):
    name = 'startsmart.campaigns'

    def ready(self):
        pass
