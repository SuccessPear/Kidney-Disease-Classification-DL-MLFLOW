from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} start <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} start <<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model training stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} start <<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e