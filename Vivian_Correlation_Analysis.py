#
# Vivian, 2025/10/22
# File: Vivian_Correlation_Analysis.py
# Short description of the task
#
import pandas as pd
from scipy import stats
# 1. Input
df = pd.read_csv('Correlation_Analysis_Data.csv')
correlation,pvalue = stats.pearsonr(df[Marketing_Spend])

# 2. Process
# print (df.isnull().sum())
# print (df.isnull().sum().sum())

# 3. Output
# print(f'Data loaded succesfully!')
# print(f'Dataset shape: {df.shape}')
print (f'Correlation: {correlation}')
print (f'P Value: {pvalue}')