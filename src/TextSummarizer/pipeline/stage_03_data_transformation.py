import os
import sys

from TextSummarizer.logging import logger
from TextSummarizer.exception import CustomException

from TextSummarizer.components.data_transformation import DataTransformationConfig, DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            data_transformation = DataTransformation()
            data_transformation.convert()
        except Exception as e:
            raise CustomException(e)