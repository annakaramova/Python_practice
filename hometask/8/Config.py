import yaml


class Config(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.read_config()

    def read_config(self):
        with open(self.config_file, 'r') as f:
            return yaml.safe_load(f)

    def get(self, key):
        return self.config[key]
