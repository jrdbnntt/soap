###
# Manages application settings
###

from copy import deepcopy

DEFAULT_SETTINGS = {
    'application_name': 'Snake',
    'application_width_min': 500,
    'application_width_initial': 500,
    'application_height_min': 500,
    'application_height_initial': 500
}


def is_setting(name):
    return name in DEFAULT_SETTINGS


class SettingsManager(object):

    def __init__(self):
        self.current = deepcopy(DEFAULT_SETTINGS)

    def set(self, setting_name, new_value):
        if is_setting(setting_name):
            self.current[setting_name] = new_value

    def get(self, setting_name):
        if is_setting(setting_name):
            return self.current[setting_name]

    def reset(self, setting_name):
        """ Sets a setting back to the default """
        if is_setting(setting_name):
            self.current[setting_name] = deepcopy(DEFAULT_SETTINGS[setting_name])

    def save(self, file_name):
        """ Saves custom settings to file """
        pass

    def load(self, file_name):
        """ Loads custom settings from file """
        pass

