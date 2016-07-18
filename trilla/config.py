# -*- coding: utf-8 -*-

import os
import yaml

TRILLA_CONFIG_HOME = "%s/.trilla" % os.path.expanduser("~")
TRILLA_CONFIG_FILE = "%s/trilla.yaml" % TRILLA_CONFIG_HOME


class ConfigurationError(Exception):
    pass

class NotConfiguredError(ConfigurationError):
    pass

class Config(object):
    def __init__(self, active_profile=None):
        """
        Contains all configuration options related to the trilla application.

        Configuration presidence:
         - command line options
         - environment variables
         - file definitions
         - defaults
        """
        # Load the defaults
        self.active_profile = active_profile
        self.target_board = "Testing Trilla"
        self.target_list = "TODO"
        self.trello = TrelloConfig()

        # If a config file exists, override existing.
        self._apply_file_values()
        self._apply_env_values()

    def update_trello(self, api_token=None, api_secret=None, oauth_token=None,
        oauth_token_secret=None):
        self.trello.update(api_token, api_secret, oauth_token,
            oauth_token_secret)

    def _apply_file_values(self):
        if not os.path.exists(TRILLA_CONFIG_FILE):
            # Nothing to do
            return

        # Load the config file.
        with open(TRILLA_CONFIG_FILE, 'r') as yaml_file:
            parsed_config = yaml.load(yaml_file)
            if not self.active_profile:
                self.active_profile = _get("default_profile", parsed_config)

            profiles = _get("profiles", parsed_config)
            if not profiles or not self.active_profile in profiles.keys():
                # TODO Try the default profile if one was configured.
                # Nothing to do
                return

            # Override values based on the selected profile
            profile = profiles[self.active_profile]
            if 'target_board' in profile:
                self.target_board = profile['target_board']
            if 'target_list' in profile:
                self.target_list = profile['target_list']
            self.trello.apply(profile)

    def _apply_env_values(self):
        # TODO Implment me!!!
        pass


class TrelloConfig(object):
    """
    Defines all config options related to the trello connection.
    """
    def __init__(self):
        self.api_key = ""
        self.api_secret = ""
        self.oauth_token = ""
        self.oauth_token_secret = ""

    def apply(self, profile_dict):
        trello_conf = profile_dict['trello']
        if not trello_conf:
            return

        self.api_key = _get('api_key', trello_conf) or self.api_key
        self.api_secret = _get('api_secret', trello_conf) or self.api_secret
        self.oauth_token = _get('oauth_token', trello_conf) or self.oauth_token
        self.oauth_token_secret = _get('oauth_token_secret', trello_conf) or self.oauth_token_secret

    def update(self, api_key=None, api_secret=None, oauth_token=None, oauth_token_secret=None):
        if api_key:
            self.api_key = api_key
        if api_secret:
            self.api_secret = api_secret
        if oauth_token:
            self.oauth_token = oauth_token
        if oauth_token_secret:
            self.oauth_token_secret = oauth_token_secret


def _get(name, config_dict, default_value=None):
    fetched = config_dict[name]
    if not fetched:
        fetched = default_value
    return fetched

