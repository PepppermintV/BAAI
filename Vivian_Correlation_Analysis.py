#
# Vivian, 2025/10/22
# File: Vivian_Correlation_Analysis.py
# Short description of the task
#
import pandas as pd

# 1. Input
df = pd.read_csv('Simple_Data.csv')
# 2. Process
print (df.isnull().sum().sum())
# 3. Output
# print(f'Data loaded succesfully')
# print(f'Dataset shape: {df.shape}')