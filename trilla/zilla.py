# -*- coding: utf-8 -*-

from __future__ import print_function
import pprint

import bugzilla

def build_query(bzapi, search_params):
    params = search_params['query']
    return bzapi.build_query(product=params.get('product', None),
        component=params.get('component', None),
        version=params.get('version', None),
        long_desc=params.get('long_desc', None),
        bug_id=params.get('bug_id', None),
        short_desc=params.get('short_desc', None),
        cc=params.get('cc', None),
        assigned_to=params.get('assigned_to', None),
        reporter=params.get('reporter', None),
        qa_contact=params.get('qa_contact', None),
        status=params.get('status', None),
        blocked=params.get('blocked', None),
        dependson=params.get('dependson', None),
        keywords=params.get('keywords', None),
        keywords_type=params.get('keywords_type', None),
        url=params.get('url', None),
        url_type=params.get('url_type', None),
        status_whiteboard=params.get('status_whiteboard', None),
        status_whiteboard_type=params.get('status_whiteboard_type', None),
        fixed_in=params.get('fixed_in', None),
        fixed_in_type=params.get('fixed_in_type', None),
        flag=params.get('flag', None),
        alias=params.get('alias', None),
        qa_whiteboard=params.get('qa_whiteboard', None),
        devel_whiteboard=params.get('devel_whiteboard', None),
        boolean_query=params.get('boolean_query', None),
        bug_severity=params.get('bug_severity', None),
        priority=params.get('priority', None),
        target_milestone=params.get('target_milestone', None),
        emailtype=params.get('emailtype', None),
        booleantype=params.get('booleantype', None),
        include_fields=params.get('include_fields', None),
        quicksearch=params.get('quicksearch', None),
        savedsearch=params.get('savedsearch', None),
        savedsearch_sharer_id=params.get('savedsearch_sharer_id', None),
        sub_component=params.get('sub_component', None),
        tags=params.get('tags', None),
        extra_fields=params.get('extra_fields'))

def get_bugs(search_params):

    URL = search_params['zilla_url']
    bzapi = bugzilla.Bugzilla(URL)
    query = build_query(bzapi, search_params)
    query['include_fields']=["id",  "bug_status", "summary", "cc", "priority", "severity"]
    bugs = bzapi.query(query)

    return bugs
