import pandas as pd
import numpy as np
import os
import sys
from src.local.logger import logging
from src.local.exception import customexception
from dataclasses import dataclass
from src.local.utils.utils import save_object
from src.local.utils.utils import evaluatemodel

from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet

class ModelTrainderConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainderConfig()

    def initiate_model_traning(self,train_array,test_array):
        try:
            logging.info("splitting dependent anf indepemdent variable from train and test")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,:-1],
                test_array[:,:-1],
                test_array[:,:-1]



            )


            models={
                'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'Elasticnet':ElasticNet()
            }


            model_report:dict=evaluatemodel(X_train,y_train,X_test,y_test)
            print(model_report)

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=best_model_name
            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customexception(e,sys)


