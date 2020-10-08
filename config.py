'''
Configuration file for sensitive settings.
Default values define here, but in production substitute with
environmental vars
'''

import os


class Config:
    SOCIAL_AUTH_FACEBOOK_APP_ID = os.environ.get(
        "SOCIAL_AUTH_FACEBOOK_APP_ID", "")

    SOCIAL_AUTH_FACEBOOK_APP_SECRET = os.environ.get(
        "SOCIAL_AUTH_FACEBOOK_APP_SECRET", "")

    SOCIAL_AUTH_FACEBOOK_APP_KEY = os.environ.get(
        "SOCIAL_AUTH_FACEBOOK_APP_KEY", "")
