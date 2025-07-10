import logging
import os
from datetime import datetime

def setup_logger(log_name:str='log'):

    os.makedirs('logs',exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m%d_%H_%M")
    log_filename = f"logs/{log_name}_{timestamp}.log"

    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # File handler
    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)

    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(name)s  %(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger