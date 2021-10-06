import logging
import os

log_file_path = os.path.abspath(os.path.join(".", os.pardir)) + "/logs/log"
LOG_FORMAT = "%(levelname)s %(filename)s line:%(lineno)d %(asctime)s - %(message)s"
logging.basicConfig(filename=log_file_path, level=logging.INFO, format=LOG_FORMAT)

TIMESTREAM_DATABASE = "coinmove"
TIMESTREAM_DATABASE_TEST = "coinmove_test"
TIMESTREAM_TABLE = "technical_data"
TIMESTREAM_TABLE_TEST = "technical_data_test"
