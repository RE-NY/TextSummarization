import os 
from pathlib import Path
import logging                               #For logging the info

#Basic logging, we will improve it once we create our own logger file.
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:') 

project_name = "TextSummarizer"

list_of_file = [
    ".github/workflows/.gitkeep", # Used for CI/CD deployment, we will make yaml file here
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_file:
    filepath = Path(filepath) #This Path converts the filepath to os readable path(eg mac mai / and widows mai \)
    filedir, filename = os.path.split(filepath)

    if(filedir != ""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file {filename}")
    if(not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        #Then create the file
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else : 
        logging.info(f"{filename} already exists.")
