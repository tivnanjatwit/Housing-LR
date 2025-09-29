import kagglehub
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Download latest version
# path = kagglehub.dataset_download("harishkumardatalab/housing-price-prediction")
# print("Path to dataset files:", path)

# Load the dataset as a pandas DataFrame
df = pd.read_csv("housing.csv")
print(df.head())