# Python
from configparser import ConfigParser
import os

# External
from bitly_api import Connection
from twitter import Twitter, OAuth

class BaseBot(object):
    def __init__(self, name):
        self._name = name
        config = ConfigParser()
        config.read('{0}.cfg'.format(self._name))
        
        oauth_token = config.get('Twitter', 'oauth_token')
        oauth_secret = config.get('Twitter', 'oauth_secret')
        consumer_key = config.get('Twitter', 'consumer_key')
        consumer_secret = config.get('Twitter', 'consumer_secret')

        self._twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, 
            consumer_key, consumer_secret))

        access_token = config.get('bitly', 'access_token')
        self._bitly = Connection(access_token=access_token)

    @classmethod
    def create_bitly_url(self, orig_url):
        data = self._bitly.shorten(orig_url)
        return data['url']

    def tweet(self, message):
        return self._twitter.statuses.update(status=message)
