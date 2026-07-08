import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(funcName)s | %(lineno)d | %(message)s"
)

logger = logging.getLogger(__name__)

def login():
    logger.info("User login")

login()