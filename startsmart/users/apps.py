from django.apps import AppConfig


print("SUUUP")
class UsersConfig(AppConfig):
    name = 'startsmart.users'

    def ready(self):
        from . import signals
