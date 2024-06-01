import os
import sys

from TextSummarizer.exception import CustomException
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import load_json

from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch

from dataclasses import dataclass
from pathlib import Path

training_params = load_json("params.json")

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path = Path("artifacts/model_trainer")
    data_path: Path = Path("artifacts/data_transformation/samsum_dataset")
    model_ckpt: Path = "google/pegasus-cnn_dailymail"
    num_train_epochs: int = training_params["num_train_epochs"]
    warmup_steps: int = training_params["warmup_steps"]
    per_device_train_batch_size: int = training_params["per_device_train_batch_size"]
    weight_decay: float = training_params["weight_decay"]
    logging_steps: int = training_params["logging_steps"]
    evaluation_strategy: str = training_params["evaluation_strategy"]
    eval_steps: int = training_params["eval_steps"]
    save_steps: float = training_params["save_steps"]
    gradient_accumulation_steps: int = training_params["gradient_accumulation_steps"]



class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def train(self):
        try:
            if not os.path.exists(os.path.join(self.model_trainer_config.root_dir,"pegasus-samsum-model")):
                device = "cuda" if torch.cuda.is_available() else "cpu"
                ## These below functions will be called from transformers library.
                tokenizer = AutoTokenizer.from_pretrained(self.model_trainer_config.model_ckpt)
                model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.model_trainer_config.model_ckpt).to(device)
                seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model = model_pegasus)
                
                #loading data 
                dataset_samsum_pt = load_from_disk(self.model_trainer_config.data_path)

                trainer_args = TrainingArguments(  ##Default function from torch/transformers
                    output_dir=self.model_trainer_config.root_dir, 
                    num_train_epochs=self.model_trainer_config.num_train_epochs, 
                    warmup_steps=self.model_trainer_config.warmup_steps,
                    per_device_train_batch_size=self.model_trainer_config.per_device_train_batch_size, 
                    per_device_eval_batch_size = 1,
                    weight_decay=self.model_trainer_config.weight_decay, 
                    logging_steps=self.model_trainer_config.logging_steps,
                    evaluation_strategy=self.model_trainer_config.evaluation_strategy, 
                    eval_steps=self.model_trainer_config.eval_steps, 
                    save_steps=self.model_trainer_config.save_steps,
                    gradient_accumulation_steps=self.model_trainer_config.gradient_accumulation_steps
                ) 

                trainer = Trainer(model = model_pegasus, args = trainer_args,
                            tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                            train_dataset=dataset_samsum_pt["train"], 
                            eval_dataset=dataset_samsum_pt["validation"])
                
                trainer.train()

                ## Save model
                model_pegasus.save_pretrained(os.path.join(self.model_trainer_config.root_dir,"pegasus-samsum-model"))
                ## Save tokenizer
                tokenizer.save_pretrained(os.path.join(self.model_trainer_config.root_dir,"tokenizer"))

                logger.info("Model and tokenizer are full-finetuned and saved.")
            else:
                logger.info(f"Model and Tokenizer already trained and exist in dir : {self.model_trainer_config.root_dir}")
        
        except Exception as e:
            raise CustomException(e)