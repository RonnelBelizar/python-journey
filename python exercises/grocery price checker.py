# 📝 Exercise: Grocery Price Checker
# Requirements:

# Ask the user how many grocery items they want to add.

# For each item, ask for:

# Item name (string)
# Item price (float)
# Store them in a dictionary like:
# {"Apples": 50.0, "Bananas": 30.0, "Milk": 75.5}

# After input, display:

# All items with their prices
# The total cost of all items
# The average price

item_number = int(input("How many: "))

cart = {}   # {"Apples": 50.0, "Bananas": 30.0, "Milk": 75.5}

for item in range(item_number):
    item_name = input("Enter Item: ")
    item_price = float(input("Enter Price: "))
    cart[item_name] = item_price

print("----------Summary----------")

for item, price in cart.items():
    print(f"{item}: {price}")

print(f"Total Cost: {sum(cart.values()):.2f}")
print(f"Average Price: {(sum(cart.values())/len(cart.values())):.2f}")
