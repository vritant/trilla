# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint

from bzilla import Bugzilla
from config import Config
from t_trello import Trello

class Trilla(object):
    def __init__(self, config):
        self.trello = Trello(config)
        self.bzilla = Bugzilla(config)

    def list_cards(self, trello_board=None, trello_list=None):
        """
        List the cards on specified board and list. Parameters are
        specified to override those in the config file.
        """
        return self.trello.get_cards(trello_board, trello_list)

    def get_bugs(self, url, cli_args, include):
        #TODO: use cli_args
        params = { 'zilla_url': url,
                   'query': { 'product':'Red Hat Enterprise Linux 7',
                              'component':'subscription-manager',
                              'status':["NEW","ASSIGNED","CLOSED"],
                              'priority':'high',
                              'bug_severity':'medium'},
                   'include': include}

        return self.yaml_wrap(self.bzilla.get_bugs(params))

    def yaml_wrap(self, entities):
        result = "---\n#Comment line to ignore:\n" + entities + "...\n"
        return result
