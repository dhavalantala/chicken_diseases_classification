from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage data ingestion started <<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage data ingestion completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage Prepare based model stage started <<<<<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>> stage Prepare based model stage completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage training  started <<<<<<<<<")
        training = ModelTrainingPipeline()
        training.main()
        logger.info(f">>>>>>> stage training completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e