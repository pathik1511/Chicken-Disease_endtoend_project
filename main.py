from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
    data_ingestion  = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<<\n\n x========================x")
except Exception as e:
    logger.exception(e)
    raise e


