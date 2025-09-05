# 📅 2025/09/05

## 📝 Topic

What I studied today:  

Did more practice exercises

## 💻 Code Example

```python
# Example code I tried
# Exercise: Sales Data Analyzer

# You are given a list of sales transactions from an online store.
# Each transaction contains:
#   - transaction_id → Unique ID of the sale
#   - customer → Name of the customer
#   - item → Item purchased
#   - quantity → Number of items bought
#   - price → Price per item (in dollars)
#
# Tasks:
# 1. Count how many transactions were made in total.
# 2. Calculate total revenue (quantity × price for each transaction).
# 3. Find out how many unique customers made purchases.
# 4. Find the best-selling item (the one with the highest total quantity sold).
# 5. Find which customer spent the most in total.

# Sample data
sales = [
    {"transaction_id": "T001", "customer": "Alice",
        "item": "Laptop", "quantity": 1, "price": 1200},
    {"transaction_id": "T002", "customer": "Bob",
        "item": "Headphones", "quantity": 2, "price": 100},
    {"transaction_id": "T003", "customer": "Alice",
        "item": "Mouse", "quantity": 1, "price": 25},
    {"transaction_id": "T004", "customer": "Charlie",
        "item": "Laptop", "quantity": 1, "price": 1200},
    {"transaction_id": "T005", "customer": "Bob",
        "item": "Keyboard", "quantity": 1, "price": 75},
    {"transaction_id": "T006", "customer": "Alice",
        "item": "Headphones", "quantity": 1, "price": 100},
]

revenue = 0
customers = set()
highest = float("-inf")
best_selling = ""
expenditure = float("-inf")
best_customer = ""

print(f"Transactions: {len(sales)}")

for data in sales:
    revenue += data["quantity"] * data["price"]
    customers.add(data["customer"])
    if data["quantity"] > highest:
        highest = data["quantity"]
        best_selling = data["item"]
    if data["quantity"] * data["price"] > expenditure:
        expenditure = data["quantity"] * data["price"]
        best_customer = data["customer"]

print(f"Revenue: ${revenue:,.2f}")
print(f"Customers: {len(customers)}")
print(f"Best selling: {best_selling}")
print(f"Best customer: {best_customer}")

```

## 🔍 Reflection

- What clicked:  

        Usage of built-in functions to pull data from a list of dictionaries

- What confused me:  

        Some syntax I tend to forget

- How I connected it to healthcare data:  

        I believe these are widely used especially in healthcare data

## 🎯 Next Step

I recently enrolled with IBM's Data Engineering Professional Certificate so I would be practicing my Python skills more in the context of Data Engineering now.
