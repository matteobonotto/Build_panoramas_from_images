from yaml import safe_load


def read_config(path):
    return ConfigFile(path)


class ConfigFile:

    def __init__(self, config_path):
        self.config_path = config_path
        with open(self.config_path, 'r') as stream:
            self.config = safe_load(stream)

        level_zero_config = self.config.get("__general__",{})

        if level_zero_config:
            assert any(key not in self.config.keys()
                       for key in level_zero_config.keys()), "conflict in conf keys"

        self.config.update(level_zero_config)

    def __getitem__(self, item):
        return self.get_section(item)

    def get_section(self, name, error="raise"):
        if error != "ignore":
            assert name in self.config.keys(), \
                "{} not in config file".format(name)

        asked_config_dict = self.config.get(name, {})
        return asked_config_dict

    def get(self, key, fallback=None):
        return self.config.get(key, fallback)
