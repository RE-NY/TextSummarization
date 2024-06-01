import os
import sys

from TextSummarizer.logging import logger
from TextSummarizer.exception import CustomException

from TextSummarizer.components.model_evaluation import ModelEvaluationConfig, ModelEvaluation


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        model_evaluation = ModelEvaluation()
        model_evaluation.evaluate()