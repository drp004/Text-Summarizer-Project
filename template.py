import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(mesaage)s:')

project_name = "TextSummarizer"

list_files = [
    ".github/workflows/.gitkeep",   # to write cicd relate files ()to implement on cloud
    f"src/{project_name}/__init__.py",    # to make constructor file. 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py",
    "research/trails.ipynb"
]


for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for this file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath == 0)):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already exists")