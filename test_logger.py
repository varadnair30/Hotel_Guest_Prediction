# from src.logger import get_logger

# logger = get_logger(__name__) #This __name__ is equivalent to the name of the current file which is test_logger. Means if you pass test_logger it is same.

# logger.info("Hello World") #Call this to log something in the log file


from src.logger import get_logger
from src.custom_exception import CustomException
import sys
logger=get_logger(__name__)

def divide_number(a,b):
    try:
        result= a/b
        logger.info("Dividing two numbers")
        return result
    except Exception as e:
        logger.error("Error occured in dividing two numbers")
        raise CustomException("Custom error zero",sys) #We are able to directly us eour custom exception clas sthis is because of the static method

if __name__=="__main__":   #This runms first when we run this file
    try:
        logger.info("Starting main programs")
        divide_number(1,0)
    except CustomException as ce:
        logger.error(ce)
        
    