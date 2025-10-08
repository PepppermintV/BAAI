#
# Vivian, 2025/10/08
# File: Vivian_Excel.py
# Short description of the task
#
import pandas as pd

# 1. Input
df =pd.read_excel('Financial_Sample.xlsx','Financial_Sample2.xlsx')
data= { }

# 2. Process

# 3. Output
sums=df.select_dtypes(include='number').sum()
print (sums)
df_combined=pd.concat([df,sums],ignore_index=True)