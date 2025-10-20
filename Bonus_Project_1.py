#import package to read excel file
import pandas as pd

#input the file address
df=pd.read_excel ('C:/Users/Vivian/OneDrive/Desktop/Business and AI/BAAI-2/sales_data.xlsx')
print (df)

print("=== Is the employee met target? ===")
for employee in df:
#     if ['Monthly_Sales'] >= ['Sales_Target']
#     target 'Yes'
#     else
#     target 'No'
    print(" ")
    print(f['Employee_Name']) 
    print(f['Monthly_Sales'])
