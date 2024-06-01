import os
import sys

from transformers import AutoTokenizer
from transformers import pipeline

from TextSummarizer.logging import logger
from TextSummarizer.exception import CustomException
from TextSummarizer.components.model_evaluation import ModelEvaluationConfig

class PredictionPipeline:
    def __init__(self):
        self.prediction_config = ModelEvaluationConfig()

    def predict(self, text): #User's provided text will be passed here.
        tokenizer = AutoTokenizer.from_pretrained(self.prediction_config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.prediction_config.model_path, tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output