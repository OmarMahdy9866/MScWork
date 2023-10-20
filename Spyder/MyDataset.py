# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:23:13 2023

@author: OmarMahdy
"""

import pandas as pd
import torch
from torch.utils.data import Dataset
import numpy as np
import math

class MyDataset(Dataset):
    """
    A custom PyTorch dataset for loading data from a CSV file and preparing it for training or testing.

    Args:
        file_name (str): The path to the CSV file containing the dataset.
        train_test_ratio (float, optional): The ratio of the dataset to be used for training (default is 0.9).
        test (bool, optional): If True, the dataset is prepared for testing; otherwise, it's prepared for training (default is False).

    Attributes:
        x_data (torch.Tensor): The input data.
        y_data (torch.Tensor): The target data.

    Methods:
        __len__(): Returns the number of samples in the dataset.
        __getitem__(idx): Returns the input and target data for a specific index.
    """

    def __init__(self, file_name, train_test_ratio=0.95, test=False):
        """
        Initializes the MyDataset with data from a CSV file.

        Args:
            file_name (str): The path to the CSV file containing the dataset.
            train_test_ratio (float, optional): The ratio of the dataset to be used for training (default is 0.9).
            test (bool, optional): If True, the dataset is prepared for testing; otherwise, it's prepared for training (default is False).
        """
        _df = pd.read_csv(file_name)

        if test:
            data_len = math.floor((1 - train_test_ratio) * len(_df.iloc[:, 0]))
        else:
            data_len = math.floor(train_test_ratio * len(_df.iloc[:, 0]))

        x = _df.iloc[:data_len, :-2].values
        y = _df.iloc[:data_len, -2:].values

        self.x_data = torch.tensor(x, dtype=torch.float32)
        self.y_data = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return np.shape(self.y_data)[0]

    def __getitem__(self, idx):
        return self.x_data[idx], self.y_data[idx]