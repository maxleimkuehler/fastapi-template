import logging

from config import DefaultConfig

log = logging.getLogger(__name__)


class CredentialService():

    def __init__(self, config=DefaultConfig()):
        self.config = config

    def apikey_exists(self, apiKey):
        try: 
            if self.config.API_KEY == apiKey:
                return True
            else:
                return False
        except Exception as ex:
            log.exception(ex)
            return False
