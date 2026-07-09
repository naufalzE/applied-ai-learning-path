import logging

logger = logging.getLogger("app")

logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(levelname)s | %(message)s"
)

console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.addHandler(console_handler)
