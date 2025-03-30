from src.DataScience.config.configuration  import ConfigurationManager
from src.DataScience.components.data_ingestion import DataIngestion
from src.DataScience import logger






class DataIngestionTrainingPipeline():
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_configuration = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_configuration)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()

STAGE_NAME = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e