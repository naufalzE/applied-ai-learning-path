import logging

logger = logging.getLogger(__name__)

# Console
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter(
        "%(levelname)s | %(message)s"
    )
)

# File
file_handler = logging.FileHandler("apps.log")
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
    )
)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

logger.info("Halo Dunia")