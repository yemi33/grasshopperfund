from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'startsmart.users'

    def ready(self):
        from . import signals
