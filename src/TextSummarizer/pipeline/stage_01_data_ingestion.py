import os
import sys
from src.TextSummarizer.logging import logger
from src.TextSummarizer.exception import CustomException

from src.TextSummarizer.components.data_ingestion import DataIngestionConfig, DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        data_ingestion = DataIngestion()
        data_ingestion.load_file()
        data_ingestion.extract_zip_file()