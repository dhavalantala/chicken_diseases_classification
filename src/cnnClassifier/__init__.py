import os 
import sys 
import logging
import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger_name = datetime.datetime.now().strftime(
    "%H_%M_%S_%d_%m_%Y.log"
)
log_filepath = os.path.join(log_dir, logger_name)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('cnnClassifierLogger')
