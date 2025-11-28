#import package to read excel file
import pandas as pd

#input the file address
df=pd.read_excel ('C:/Users/Vivian/OneDrive/Desktop/Business and AI/BAAI-2/sales_data.xlsx')
total_target=[]
total_bonus=[]

print("SALES PERFORMANCE REPORT")
print("========================")
for idx, employee in df.iterrows():
    if employee['Monthly_Sales'] >= employee['Sales_Target']:
        target='MET'
        bonus=employee['Monthly_Sales'] * 0.1
    else:
        target='NOT MET'
        bonus=employee['Monthly_Sales']*0.05
    total_target.append(target)
    total_bonus.append(bonus)
    print(f"Employee Name: {employee['Employee_Name']}|Target {target}|Sales: ${employee['Monthly_Sales']}|Bonus:${bonus}")
print(" ")
print(f"Total Bonuses to pay: ${sum(total_bonus)}")