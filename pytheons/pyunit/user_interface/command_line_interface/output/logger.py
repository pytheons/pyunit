import logging
import logging.config
import os

import yaml


class LoggerFactory:
    @staticmethod
    def setup():
        path = os.path.abspath('{}/../../../config/'.format(os.path.dirname(__file__)))
        with open('{}/logging.yaml'.format(path), 'rt') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)

        return logging.getLogger('pyunit')


logger = LoggerFactory.setup()
