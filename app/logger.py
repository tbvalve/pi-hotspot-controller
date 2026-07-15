import logging
from app.config import config

def setup_logger():
    logging.basicConfig(
        filename=config.LOG_FILE,
        level=logging.INFO,
        format=\"%(asctime)s | %(levelname)s | %(message)s\"
    )
    return logging.getLogger(\"HotspotController\")

logger = setup_logger()
