import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("nopCommerce")
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers
        if not logger.handlers:
            log_dir = "/home/ethan/PycharmProjects/nopcommerceApp/Logs"
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, "automation.log")

            fh = logging.FileHandler(log_file, mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%y %I:%M:%S %p')
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger
