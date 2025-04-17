#We cannot directly use the IAM user account for data ingestion in vs code. We need to use service account for that. 
# Run in terminal: set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\satya\Downloads\analog-medium-456413-q6-51d3011d5c74.json -> This gives the access to the storage and bucket from GCP now you can run here also.
# Do this after creating service account and setting the permission to Storage Admin and Storage object viewer to both the IAM and service account.

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from google.cloud import storage
from google.oauth2 import service_account
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import * #All the paths get imported here.
from utils.common_functions import read_yaml_file

logger=get_logger(__name__)

##Most important concepts of OOPS
# What is the use of self in python? So first the differece between method and function is that the method is a part of the class(it is also a function but inside the class) and function is not a part of the class.
#To access the instance variable of one method in another method we use self.

# class Dog:      This is class
#     def __init__(self, name):  Method(Function) of the class.
#         self.name = name    Name is the instance variable/attribute. So if we donot write self we cannot access the instance variable from another method within the class.
#This variable is then available to other methods in the class that use self

# my_dog = Dog("Buddy")  # <-- my_dog is an object (or instance)

#my_dog.name  # 'name' is an instance variable of the object 'my_dog'. This will return Buddy, this is possible because of __init__. 
# This is called constructor which python expects at the time of object creation to access the instance(object) variable(attribute). Note if you use other method like say dog_char isntead of __init__ and access the variables using dog_char.name it will not return.

#Remember static methods also are the attributes or instance variables of the class/object. So we can access them using self. But this is not good practice. Always try to access static method it using class name. Static metjod donot use self


# __init__ is a special method in Python classes, also known as a constructor.
#It gets called automatically when you create an object of the class.


# We can call any static or non static methods inside any other non static method using self.
#But We cannot access non static method inside static method directly using self
#To access the variable in another class write self.variable=XYZ. Donot write variable=XYZ.     

#If it is a nomrla method you need to pass self even though you donot need to access the self variables from other methods iniside the class. If you donot want to use then you can pass @staticmethod

class DataIngestion:
    def __init__(self,config):
        self.config=config["data_ingestion"]
        self.bucket_name=self.config["bucket_name"]
        self.file_name=self.config["bucket_file_name"]
        self.train_ratio=self.config["train_ratio"]
        
        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info(f"Data Ingestion is started with {self.bucket_name} and file is {self.file_name} ")
        self.raw_data_dir=RAW_FILE_PATH # We can access all variables because of from config.paths_config import *
        self.train_data_dir=TRAIN_FILE_PATH
        self.test_data_dir=TEST_FILE_PATH
        
    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name) #So to access blob in another method we eed to use self.blob=bucket.blob....
            blob.download_to_filename(self.raw_data_dir) #raw.csv 
            logger.info(f"CSV file is successfully downloaded to {self.raw_data_dir}")
        except Exception as e:
            logger.error("Error downloading the csv file")
            raise CustomException("Failed to download the csv file",e)
        
    def split_data(self):
        try:
            logger.info("Splitting the data into train and test")
            data=pd.read_csv(self.raw_data_dir) 
            
            train_data, test_data = train_test_split(data,test_size=1-self.train_ratio, random_state=42) # data frames of train and test
            
            train_data.to_csv(self.train_data_dir,index=False) #Dataframe is converted to csv for train and test
            test_data.to_csv(self.test_data_dir,index=False)
            logger.info("Data is successfully splitted into train and test")
        except Exception as e:
            logger.error("Error splitting the data")
            raise CustomException("Failed to split the data into train and test",e)
        
    def run(self):
        try:
            logger.info("Data Ingestion is started")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data Ingestion is completed")
        except CustomException as ce:
            logger.error(f"CustomExeption:{ce}")
        
if __name__=="__main__":
    data_ingestion=DataIngestion(read_yaml_file(CONFIG_PATH))
    data_ingestion.run()
    
            
        