#
# Vivian, 2025/10/08
# File: Vivian_Excel.py
# Short description of the task
#
import pandas as pd
import os
from glob import glob

# 1. Input
folder_path ='C:/Users/Vivian/OneDrive/Desktop/Business and AI/BAAI-1'
excel_files = [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xls'))]

all_dataframes = []
for file_name in excel_files:
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_excel(file_path)
    all_dataframes.append(df)

# 2. Process

# 3. Output
sums=df.select_dtypes(include='number').sum()
print (sums)
df_combined=pd.concat([df,sums],ignore_index=True)