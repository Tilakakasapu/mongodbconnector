import os
from pathlib import Path 
package_name = "mongodb_connect"
list_of_files =[
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py"
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]

for i in list_of_files:
    i = Path(i)
    file_dir,filename = os.path.split(i)
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        
    
    if(not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open(i,"w") as f:
            pass

