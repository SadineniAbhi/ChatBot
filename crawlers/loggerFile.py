import logging
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir+'/data', "logs.log")

logger = logging.getLogger(__name__)
f_handler = logging.FileHandler(file_path)
f_handler.setLevel(logging.WARNING)
logger.addHandler(f_handler)


