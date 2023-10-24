from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_based_model import PrepareBaseModel
from cnnClassifier import logger 

STAGE_NAME = "Prepare based model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage prepare base model started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage prepare base model completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e