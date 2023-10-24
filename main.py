from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from cnnClassifier.config.configuration import ConfigurationManager



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


STAGE_NAME = "Prepare Training Components"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        training = ModelTrainingPipeline()
        training.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Elalution classifier"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e