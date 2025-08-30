# 📅 2025/08/30

## 📝 Topic

1. Concession Stand Exercise
    - Utilized loops
    - Dict data manipulation
        - Store, write, pull

## 💻 Code Example

```python
# Concession Stand Simulator — Exercise
# -------------------------------------------------------
# Your task:
# Build a console program that simulates a concession stand
# where customers can order food items, pay, and receive change.
# The program should also keep track of sales and inventory.
#
# Features to implement:
# 1. Menu (dict: item → price)
# 2. Inventory (dict: item → quantity)
# 3. Place orders (loop until customer is done)
# 4. Check inventory before confirming an order
# 5. Compute total cost of an order
# 6. Accept payment and calculate change
# 7. Update inventory after a sale
# 8. Print a receipt
# 9. Track sales for the day
# 10. Show daily summary at the end
# -------------------------------------------------------

import time

menu = {
    "Popcorn": 120.00,
    "Soda": 60.00,
    "Hotdog": 85.00,
    "Nachos": 140.00,
    "Candy": 50.00
}

inventory = {
    "Popcorn": 20,
    "Soda": 30,
    "Hotdog": 15,
    "Nachos": 10,
    "Candy": 25
}

for food, price in menu.items():
    print(f"{food:10}: ${price:.2f}")

orders = {}     # Dict of orders
total_cost = 0

while True:
    order = input("What are your orders? (q to quit): ").title()
    if order == "Q":
        break
    if order not in menu:   # Prevent invalid input
        print("Sorry, that item is not on the menu.")
        continue
    qty = int(input("How many?: "))

    for food, stock in inventory.items():  # Inventory checker
        if order == food:
            if qty <= stock:
                inventory[food] = stock - qty
                print(f"Remaining {food}: {inventory[food]}")
            else:
                print(f"Maximum order for {food} is {stock} pc/s.")
                qty = 0  # cancel this order
            break   # no need to keep looping

    for item, price in menu.items():    # Ordering
        if order == item and qty > 0:
            if order in orders:
                orders[order] += price * qty  # accumulate instead of overwrite
            else:
                orders[order] = price * qty

    print("------------------------------")

for item, price in orders.items():      # Calculating total cost
    total_cost += price

print("------------------------------")
print(f"Your total bill: ${total_cost:.2f}")
print("------------------------------")

# allow decimal payments
payment = float(input("Enter amount of payment: "))
change = payment - total_cost
print("------------------------------")
print(f"Your change: ${change:.2f}")
print("------------------------------")
print("Thank you for purchasing!")

time.sleep(3)

print("------------------------------")
print("Inventory: ")
for item, stock in inventory.items():
    print(f"{item:15}: {stock} ")
print(f"Total Sales: ${total_cost:.2f}")
```

## 🔍 Reflection

- What clicked:  

    - Loops and dict data manipulation.

- What confused me:  

    - Nested loops can sometimes be confusing.

- How I connected it to healthcare data:  

    - This could be useful as there are tons of health care data to be manipulated.

## 🎯 Next Step

Proceed with BroCode's timestamp 3:19:30
