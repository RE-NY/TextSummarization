import os
import sys

from TextSummarizer.logging import logger
from TextSummarizer.exception import CustomException

from TextSummarizer.components.model_trainer import ModelTrainerConfig, ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        model_trainer = ModelTrainer()
        model_trainer.train()