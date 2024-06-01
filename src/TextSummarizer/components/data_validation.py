import os 
import sys
from TextSummarizer.logging import logger
from TextSummarizer.exception import CustomException

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path = Path("artifacts/data_validation")
    STATUS_FILE: str = "artifacts/data_validation/status.txt"
    ALL_REQUIRED_FILES = ["train", "test", "validation"]


class DataValidation:
    def __init__(self):
        self.data_validation_config = DataValidationConfig()


    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            
            os.makedirs(self.data_validation_config.root_dir, exist_ok = True)
            for file in all_files:
                if file not in self.data_validation_config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.data_validation_config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.data_validation_config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise CustomException(e)