import os
import sys
import pandas as pd
import numpy as np

from src.local.logger import logging
from src.local.exception import customexception
from src.local.utils.utils import save_object
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

class DataTransformationConfig:
    preprocessor_obj_file=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    def get_data_tranformation(self):

        try:
            logging.info("data transformation started")

            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']


            logging.info("pipeline initiated")

            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )


            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencode',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories]))
                ]
            )


            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])


            return preprocessor
        


        except Exception as e:
            raise customexception(e,sys)
        


    def initiate_data_trandormation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completed")
            logging.info(f'train dataframe head : \n{train_df.head().to_string()}')
            logging.info(f'test dataframe head : \n{test_df.head().to_string()}')

            preprocessor_obj=self.get_data_tranformation()


            target_column_name='price'
            drop_column=[target_column_name,'Unnamed:0']

            input_feature_train_df=train_df.drop(columns=drop_column,axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=drop_column,axis=1)
            target_feature_test_df=test_df[target_column_name]

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            logging.info("applying preprocessing on train and test data")

            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file,
                obj=preprocessor_obj
            )

            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )

        except Exception as e:
            raise customexception(e,sys) 
