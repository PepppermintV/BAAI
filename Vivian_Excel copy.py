#
# Vivian, 2025/10/08
# File: Vivian_Excel.py
# Short description of the task
#
import pandas as pd
import os
from glob import glob

# 1. Input
df = pd.read_excel ('C:/Users/Vivian/OneDrive/Desktop/Business and AI/BAAI-1/Financial_Sample.xlsx')
# 2. Process

# 3. Output
sums=df.select_dtypes(include='number').sum()
# print (sums)
sums_row = pd.DataFrame([sums])
df_combined=pd.concat([df,sums],ignore_index=True)
df_combined.to_excel('C:/Users/Vivian/OneDrive/Desktop/Business and AI/BAAI-1/Financial_Sample.xlsx', index=False)
print(df_combined)
