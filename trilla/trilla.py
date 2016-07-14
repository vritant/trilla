# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint

import zilla
from config import Config
from t_trello import Trello


class Trilla(object):
    def __init__(self, config):
        self.trello = Trello(config)

    def list_cards(self, trello_board=None, trello_list=None):
        """
        List the cards on specified board and list. Parameters are
        specified to override those in the config file.
        """
        return self.trello.get_cards(trello_board, trello_list)

    # TODO Move this into an bugzilla object.
    def get_bugs(self, url):
        params = { 'zilla_url': url,
                   'query': { 'product':'Red Hat Enterprise Linux 7',
                              'component':'subscription-manager',
                              'status':["NEW","ASSIGNED","CLOSED"],
                              'priority':'high',
                              'bug_severity':'medium'}}
        bugs = zilla.get_bugs(params)
        return bugs
