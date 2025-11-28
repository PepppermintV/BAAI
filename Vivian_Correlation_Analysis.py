#
# Vivian, 2025/10/22
# File: Vivian_Correlation_Analysis.py
# Short description of the task
#
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Input
df = pd.read_csv('Correlation_Analysis_Data.csv')
df.info()
print (df.isnull().sum())
print (df.isnull().sum().sum())
correlation_matrix=df.iloc[:,1:6].corr()
print(correlation_matrix.round(3))
print( df.iloc[:,1:6])
correlation,pvalue = stats.pearsonr(df['Marketing_Spend'],df['Sales_Revenue'])

# 2. Process
# df[].corr()


# 3. Output
print(f'Data loaded succesfully!')
print(f'Dataset shape: {df.shape}')
print (f'Correlation: {correlation:.2f}')
print (f'P Value: {pvalue}')
sns.heatmap (correlation_matrix)
plt.title ('Vivian is the most intelligent person in the world')
plt.tight_layout()
plt.show()

print (df.head(5))
print (df.tail(5))