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
        if not os.path.exists(TRILLA_CONFIG_FILE):
            raise NotConfiguredError("Trilla is not yet configured.")
        
        # Load the config file.
        with open(TRILLA_CONFIG_FILE, 'r') as yaml_file:
            parsed_config = yaml.load(yaml_file)

        if not active_profile:
            active_profile = parsed_config['default_profile']
        
        profiles = get("profiles", parsed_config)
        if not active_profile in profiles.keys():
            raise ConfigurationError("Specified profile '%s 'does not exist!" % active_profile)
        
        profile = profiles[active_profile]


def get(section, config_dict):
    if not section in config_dict.keys():
        raise ConfigurationError("Config section not found: %s" % section)
    return config_dict[section]

