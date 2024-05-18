from crawlers.removeEmptyLines import removeEmptyLines
import os
from crawlers.loggerFile import logger
def write_data(data):
    data = removeEmptyLines(data)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    #creates the data file probly unsafe to do +/data fix would be appreiciated!!
    file_path = os.path.join(script_dir+'/data', "scrapped_data.txt")
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(data)
    except FileNotFoundError:
        logger.error("File not found!")
    except PermissionError:
        logger.error("Permission denied!")
    except Exception as e:
        logger.critical("An error occurred:", e)



