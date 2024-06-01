import os 
import sys 
from dataclasses import dataclass
from pathlib import Path
import urllib.request as request
import zipfile
import shutil

from TextSummarizer.logging import logger    # For logging
from TextSummarizer.utils.common import read_yaml, create_directories, get_size
from TextSummarizer.exception import CustomException

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: str = "artifacts/data_ingestion"
    source_path: Path = Path("research/dataset/archive.zip")
    saved_file_path: str = os.path.join("artifacts/data_ingestion", "data.zip")
    unzip_dir: str = "artifacts/data_ingestion"


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    
    def load_file(self):
        try:
            if not os.path.exists(self.ingestion_config.saved_file_path):
                # filename, headers = request.urlretrieve(
                #     url = self.config.source_URL,
                #     filename = self.config.local_data_file
                # )
                os.makedirs(self.ingestion_config.root_dir, exist_ok=True)
                shutil.copy(self.ingestion_config.source_path, self.ingestion_config.saved_file_path)
                logger.info("Dataset Copied and loaded!")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.ingestion_config.saved_file_path))}")  
        except Exception as e:
            raise CustomException(e)

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            os.makedirs(self.ingestion_config.unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.ingestion_config.saved_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.ingestion_config.unzip_dir)
            logger.info(f"Zip File extracted and save in dir : {self.ingestion_config.unzip_dir}")
        except Exception as e:
            raise CustomException(e)


if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.load_file()
    data_ingestion.extract_zip_file()

