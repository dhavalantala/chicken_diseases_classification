from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage Data Ingestion stage started <<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage Data Ingestion stage completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)