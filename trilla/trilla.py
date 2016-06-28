# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint

import zilla
import trello

def get_bugs(url, cli_args):
    #TODO: use cli_args
    params = { 'zilla_url': url,
               'query': { 'product':'Red Hat Enterprise Linux 7',
                          'component':'subscription-manager',
                          'status':["NEW","ASSIGNED","CLOSED"],
                          'priority':'high',
                          'bug_severity':'medium'}}

    bugs = zilla.get_bugs(params)
    return bugs
