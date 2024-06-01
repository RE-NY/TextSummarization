import os
import sys
from TextSummarizer.logging import logger
from TextSummarizer.exception import CustomException

from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path = "artifacts/data_transformation"
    data_path: Path = "artifacts/data_ingestion/samsum_dataset"
    tokenizer_name: Path = "google/pegasus-cnn_dailymail"  #Enter for huggingface!


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.tokenizer = AutoTokenizer.from_pretrained(self.data_transformation_config.tokenizer_name)


    
    def convert_examples_to_features(self,example_batch):
        try:
            input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
            
            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
            logger.info("Successfully converted examples to features")
            return {
                'input_ids' : input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        except Exception as e:
            raise CustomException(e)
    

    def convert(self):
        try:
            if not os.path.exists(self.data_transformation_config.root_dir):
                dataset_samsum = load_from_disk(self.data_transformation_config.data_path)
                dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
                dataset_samsum_pt.save_to_disk(os.path.join(self.data_transformation_config.root_dir,"samsum_dataset"))
                logger.info(f"Successfully converted dataset and save to dir : {self.data_transformation_config.root_dir}")
            else :
                logger.info(f"Converted dataset is already converted and saved in dir : {self.data_transformation_config.root_dir}")
        except Exception as e:
            raise CustomException(e)
        