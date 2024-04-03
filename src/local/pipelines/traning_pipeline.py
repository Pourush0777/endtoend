from src.local.components.data_ingestion import DataIngestion

from src.local.components.data_transformation import DataTransformation

from src.local.components.model_trainer import ModelTrainer

from src.local.components.utils.utils import evaluatemodel



import os
import sys
from src.local.logger import logging
from src.local.exception import customexception
import pandas as pd

obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

model_trainer_obj=ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr,test_arr)