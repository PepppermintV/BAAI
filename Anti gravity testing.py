import pandas as pd

# Create a sample DataFrame
data = {
    'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'Annual_Spend': [3500, 4200, 1500, 8000, 5000]
}
df = pd.DataFrame(data)

# Create a new DataFrame called high_value_customers that only includes customers with
# an Annual_Spend greater than or equal to $4,000
high_value_customers = df[df['Annual_Spend'] >= 4000].copy()

# Sort this new filtered DataFrame in descending order by Annual_Spend
high_value_customers = high_value_customers.sort_values(by='Annual_Spend', ascending=False)

# Print the result
print(high_value_customers)
