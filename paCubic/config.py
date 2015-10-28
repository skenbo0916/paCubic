import configparser


class Config:

    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read('config.ini')

    def get_config(self):
        return self.config
