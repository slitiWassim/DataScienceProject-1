import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "DataScience"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/comstants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html" 
]




for filepath in list_of_files:
    filepath = Path(filepath)
    folder_dir , filename = os.path.split(filepath)

    if folder_dir != "":
        os.makedirs(folder_dir,exist_ok=True)
        logging.info(f"Creating directory {folder_dir} for the file : {filename}")

    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) ):

        with open(filepath,mode="w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists")