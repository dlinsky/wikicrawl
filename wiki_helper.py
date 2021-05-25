import requests as req
import random
import json
import wikipediaapi


class WikiHelper(object):
    def __init__(self):
        self.session = req.Session()
        self.URL = "https://en.wikipedia.org/w/api.php"
        self.wiki = wikipediaapi.Wikipedia('en')

    def get_url(self, topic):
        return self.wiki.page(topic)
