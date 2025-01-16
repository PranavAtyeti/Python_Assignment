import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("my_package.log"),  # Logs to a file
        logging.StreamHandler()                # Logs to the console
    ]
)

logger = logging.getLogger("my_package")
