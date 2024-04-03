import os
from pathlib import Path

package_name="local"

list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py"
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/traning_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/eda.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py"
    
   
]


for i in list_of_files:
    i=Path(i)
    filedir,filename=os.path.split(i)


    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open (i,"w") as f:

            pass
    else:
        print("file already exists")