import logging
import sys
import os

# SECRETS
DATABASE_URL = os.getenv('DATABASE_URL')

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
