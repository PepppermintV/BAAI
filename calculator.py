products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}]

#the empty list to store all the discount, and then to calculate at the end
discounted_product= []
discount_amounts=[]
#initial price and discount
total_final_price=0
total_final_discount=0
total_product = len(products)
total_original = sum(product['price'] for product in products)
print("=== PRODUCT DISCOUNT CALCULATOR ===")   
for product in products:
    if product['category']== "Electronics":
        if product['price']>=1000:
            discount_percent = 20
        elif product['price']>=500:
            discount_percent = 15
        else:
            discount_percent = 10
    elif product['category']== "Clothing":
        if product['price']>=100:
            discount_percent = 25
        else:
            discount_percent = 15
    elif product['category']== "Books":
        discount_percent = 10
    else:
        discount_percent = 0
    discount_amount = (product['price'] * discount_percent / 100)
    final_price = product['price'] - discount_amount
    total_final_price+=final_price
    total_final_discount+=discount_amount
    discounted_product.append((discount_amount,product))
    discount_amounts.append((discount_amount))
    print(" ")
    print(f"Product: {product['name']}")
    print(f"Category: {product['category']}")
    print(f"Original Price: ${product['price']}")
    print(f"Discount: {discount_percent}%")
    print(f"Final Price: ${final_price}")

print(" ")
print("=== SUMMARY ===")        
print(f"Total Products: {total_product}")
print(f"Total Original Price: ${total_original}")
print(f"Total Discount: ${total_final_discount}")
print(f"Total Final Price: ${total_final_price}")

max_product_tuple=max(discounted_product, key=lambda x: x[0])
max_discount = max_product_tuple [0]
max_discount_product = max_product_tuple [1]
average_discount=sum(discount_amounts)/len(discount_amounts)
print(" ")  
print("===Product with highest discount===")
print(f"product name:{max_discount_product['name']} ")
print(f"discount: ${max_discount} ")
print(f"average discount across all product: $ {average_discount:.2f}")

print("")
print("The most expensive and cheapest product")
