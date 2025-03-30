import  urllib.request as  request
from src.DataScience import logger
from src.DataScience.entity.config_entity import (DataIngestionConfig)
import zipfile
import os





## Components-Data Ingestion
class DataIngestion :
    def __init__(self,
                 config:DataIngestionConfig):
        self.config = config
    
    ## Downloading the zip file 
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded ! with following info \n{header}") 
        else :
            logger.info(f"{filename} File already exists !! ")
    
    ## Unzip file
    def extract_zipfile(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref :
            zip_ref.extractall(unzip_path)


