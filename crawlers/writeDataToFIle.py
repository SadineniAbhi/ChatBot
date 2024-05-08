from .removeEmptyLines import removeEmptyLines
import os
from .CustomError import CustomError

def write_data(data):
    data = removeEmptyLines(data)
    script_dir = os.path.dirname(os.path.abspath(__file__))#creates the data file
    # probly unsafe to do +/data fix would be appreiciated!!
    file_path = os.path.join(script_dir+'/data', "scrapped_data.txt")
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(data)
    except:
        raise CustomError("Unable to write data to the file")
        


