# 📅 2025/09/09

## 📝 Topic

Cheapest Product Checker

## 💻 Code Example

```python
# Cheapest seller with the cheapest product

import time
inventory = {}   # {name : {fruit:price}}
while True:
    products = {}   # {fruit:price}

    vendor = input(
        "Enter vendor name (input \"x\" to proceed to the question): ").lower()
    if vendor == "x":
        break

    qty = int(input("How many items?: "))

    for x in range(qty):
        item = input(f"Item {x+1}: ")
        price = int(input(f"Price {x+1}: "))
        products[item] = price

    inventory[vendor] = products
print("------" * 6)
print("Determining the cheapest product of a vendor...")
time.sleep(2)
print("------" * 6)
print(*inventory)
while True:
    ask = input(
        "Do you want to know who sells the cheapest product? \"y\" to proceed \"x\" to quit: ").lower()

    if ask == "x":
        time.sleep(2)
        print("Exiting program")
        break

    fruit = input("Enter fruit: ").lower()

    lowest = float("inf")
    vendor_lowest = ""
    cheapest_fruit = ""

    for vendor, products in inventory.items():
        if fruit in products and products[fruit] < lowest:
            lowest = products[fruit]
            vendor_lowest = vendor
            cheapest_fruit = fruit
    print("------" * 6)
    if vendor_lowest:
        print(
            f"Vendor: {vendor_lowest:20} \nProduct: {cheapest_fruit} \nPrice: PHP {lowest:,.2f}")
    else:
        print("No vendor has this product")
    print("------" * 6)

```

## 🔍 Reflection

- What clicked:  
    
    Nested loops, dictionary within a dictionary

- What confused me:  

    Since it is a nested loop, syntax can be sometimes confusing

- How I connected it to healthcare data:  

    I think this is a perfect exercise for pulling data from a dictionary within a dictionary — which I think would be a common practice for healthcare data

## 🎯 Next Step

Focused on IBM Data Engineering Coursera course
