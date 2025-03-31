from src.DataScience.config.configuration  import ConfigurationManager
from src.DataScience.components.data_transformation import DataTransformation
from src.DataScience import logger
from pathlib import Path






class DataTransformationTrainingPipeline():
    def __init__(self):
        pass
    def initiate_data_transformation(self):

        try :
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status  ==  "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("You data schema is not valid")
            
        except Exception as e:
            print(e)    

STAGE_NAME = "Data Transformation Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e