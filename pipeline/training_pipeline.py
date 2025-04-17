from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessing
from src.model_training import ModelTraining
from config.paths_config import *
from utils.common_functions import read_yaml_file

if __name__=="__main__":
    ## Data Ingestion
    data_ingestion=DataIngestion(read_yaml_file(CONFIG_PATH))
    data_ingestion.run()
    
    
    ### Data Preprocessing
    data_preprocessing=DataPreprocessing(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    data_preprocessing.process()
    
    ### Model Training
    model_training=ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    model_training.run()