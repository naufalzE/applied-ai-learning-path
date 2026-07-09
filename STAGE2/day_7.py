import logging

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")

file_handler.setFormatter(
    logging.Formatter(
        "%(levelname)s | %(message)s"
    )
)

logger.addHandler(file_handler)

# ==========================================
# Logger memiliki 1 handler
# ==========================================

logger.info("Halo Dunia")

# ==========================================
# Menambahkan handler kedua
# ==========================================

console2 = logging.StreamHandler()

console2.setFormatter(
    logging.Formatter("SECOND >> %(message)s")
)

logger.addHandler(console2)

# ==========================================
# Logger sekarang memiliki 2 handler
# ==========================================

logger.info("Halo Lagi")