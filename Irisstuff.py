import sklearn
import numpy as np
import pandas as pd
import os

import kagglehub

# Download latest version
path = kagglehub.dataset_download("uciml/iris")

print("Path to dataset files:", path)

# Load the dataset
file_path = os.path.join(path, "Iris.csv")
df = pd.read_csv(file_path)

# Get feature names
feature_names = df.columns
print("Feature names:", feature_names)

print("First 5 records:", df.head())