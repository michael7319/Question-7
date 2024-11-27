# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZYEApd6QA5ZwNLcibTlf0Db3xqLQlGt
"""



"""IMPORT THE LIBRARIES"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import string
import random
import pandas as pd
import matplotlib.pyplot as plt

"""DEVICE CONFIG"""

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

"""FUNCTIONS FOR DATA PREPROCCESSING"""

all_letters = string.ascii_lowercase + " "
n_letters = len(all_letters)

def letter_to_index(letter):
    return all_letters.find(letter.lower())

def name_to_tensor(name):
    """Turn a name into a tensor of shape (name_length, n_letters)"""
    tensor = torch.zeros(len(name), n_letters)
    for li, letter in enumerate(name):
        tensor[li][letter_to_index(letter)] = 1
    return tensor

"""CREATING THE DATASET"""

data = {
    "name": ["Emily", "John", "Alice", "Tom", "David", "Sophia", "Michael", "Emma", "George", "Olivia"],
    "gender": ["Female", "Male", "Female", "Male", "Male", "Female", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)

df['gender'] = df['gender'].apply(lambda x: 0 if x == "Female" else 1)

class NameGenderDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        name = self.data.iloc[idx, 0]
        gender = self.data.iloc[idx, 1]
        return name_to_tensor(name), torch.tensor(gender, dtype=torch.long)

dataset = NameGenderDataset(df)
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)