products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}]

for product in products:
    print(f"Name: {product['name']}, Price: ${product['price']}, Category: {product['category']}")
for product in products:
    category = product ['category']

#if category= "Electronics"
#print("Total product: {total_product}","Total original price":{total_original_price},"Total discount:{}", "Total revenue:{}")