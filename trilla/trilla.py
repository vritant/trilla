# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint

import zilla
from config import Config
from t_trello import Trello


class Trilla(object):
    def __init__(self, profile):
        config = Config(profile)
        self.trello = Trello(config)
    
    def list_cards(self):
        return self.trello.get_cards("TODO")


    def get_bugs(self, url):
        params = { 'zilla_url': url,
                   'query': { 'product':'Red Hat Enterprise Linux 7',
                              'component':'subscription-manager',
                              'status':["NEW","ASSIGNED","CLOSED"],
                              'priority':'high',
                              'bug_severity':'medium'}}
        bugs = zilla.get_bugs(params)
        return bugs
