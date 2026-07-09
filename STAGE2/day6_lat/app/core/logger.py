import logging

logger = logging.getLogger("app")

if len(logger.handlers) == 0:

    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(levelname)s | %(message)s"
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)