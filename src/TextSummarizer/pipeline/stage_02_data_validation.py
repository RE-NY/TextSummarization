import os
import sys
from TextSummarizer.components.data_validation import DataValidationConfig, DataValidation
from TextSummarizer.exception import CustomException
from TextSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            data_validation = DataValidation()
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise CustomException(e)


