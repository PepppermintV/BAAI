products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}]

print("=== PRODUCT DISCOUNT CALCULATOR ===")   
for product in products:
    if product['category']== "Electronic":
        if product['price']>=1000:
            discount_percent = 20
        elif product['price']>=500:
            discount_percent = 15
        else:
            discount_percent = 10
        discount_price = product['price'] - (product['price'] * discount_percent / 100)
        print(f"Product: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Original Price: ${product['price']}")
        print(f"Discount: {discount_percent}%")
        print(f"Final Price: ${discount_price}")
        print(" ")
    if product['category']== "Clothing":
        if product['price']>=100:
            discount_percent = 25
        else:
            discount_percent = 15
        discount_price = product['price'] - (product['price'] * discount_percent / 100)
        print(f"Product: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Original Price: ${product['price']}")
        print(f"Discount: {discount_percent}%")
        print(f"Final Price: ${discount_price}")
        print(" ")
    if product['category']== "Books":
        discount_percent = 10
        discount_price = product['price'] - (product['price'] * discount_percent / 100)    
        print(f"Product: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Original Price: ${product['price']}")
        print(f"Discount: {discount_percent}%")
        print(f"Final Price: ${discount_price}")
        print(" ")

total_product = len(products)
total_original = sum(product['price'] for product in products)
total_discount = sum(discount_percent for product in products)
total_final = sum(discount_price for product in products)


print("=== SUMMARY ===")        
print(f"Total Products: {total_product}")
print(f"Total Original Price: ${total_original}")
print(f"Total Discount: ${total_discount}")
print(f"Total Final Price: ${total_final}")



