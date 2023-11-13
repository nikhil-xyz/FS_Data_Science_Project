import numpy as np
import pandas as pd
import os
from src.DimondPricePrediction.logger import logging

from sklearn.model_selection import train_test_split
from src.DimondPricePrediction.exception import customexception
from dataclasses import dataclass
from pathlib import Path

class DataIngestion:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        logging.info('Data Injestion Started')

        try:
            data = pd.read_csv(os.path.join('notebook/data', 'gemstone.csv'))
            logging.info('I have read the dataset as a dataframe')

            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info('train_test_split completed')
        except Exception as e:
            pass
