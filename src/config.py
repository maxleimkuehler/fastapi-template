import os
import logging


class DefaultConfig:
    # APIKEY
    API_KEY = os.environ.get("API_KEY", "")

    logging.basicConfig(level=os.environ.get("LOGLEVEL", "WARNING"))
