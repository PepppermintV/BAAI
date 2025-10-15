#
# Vivian, 2025/10/15
# File : Vivian_IF.py
#

# 1. Input
# Temperature = int(input("Temperature: "))
# if Temperature > 25:
#     print("It's too hot outside, Study hard in the library")

# 2. Process
# for i in range (1,6):
#     if i >=5:
#         print(f"count {i}", end=' ')
#     else:
#         print(f"count {i}", end=' ')

order_value =[120, 450, 80, 300, 650]
total_revenue= 0

for order in order_value:
    total_revenue+=order
    print(f"Processing order:${order}")
    
total_item =order_value.count(order)
print (f"\nTotal Revenue: ${total_revenue}")
print (f"\nTotal Item:${total_item}")
# 3. Output