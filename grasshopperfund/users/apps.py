from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'grasshopperfund.users'

    def ready(self):
        from . import signals
