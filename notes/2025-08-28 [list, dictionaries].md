# 📅 2025/08/28

## 📝 Topic

What I studied today:  

1. Exercise about list
2. Exercise about dictionary
3. New functions such as
    - dict.values()
        - In a dict, there are key:value pair of data
        - In this function, it accesses the values eg [90, 23, 32]
    - dict.items()
        - In a dict, it accesses the contents. Sample,
            - for item, price in dict.items()
    - var = float("-inf") or var = float("inf")
        - Used for comparing max or min values in a list or dict
4. Did a few healthcare related data exercises

## 💻 Code Example

```python
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


————————————————————————————————————————————————————————————————————————————————————————————————————————————

# 📝 Exercise: Student Score Tracker
# Requirements:

# Ask how many students are in the class.

# For each student, ask for:

# Student name (string)
# Student score (integer)
# Store them in a dictionary like:

# {"Alice": 90, "Bob": 76, "Charlie": 85}

# After input, display:

# Each student with their score.
# The highest score and which student got it.
# The lowest score and which student got it.
# The class average.

num_students = int(input("How many students?: "))

grades = {}

for num in range(num_students):
    name = input("Enter name: ")
    score = int(input("Score: "))
    grades[name] = score

print("---------------SUMMARY---------------")

highest_student = ""
lowest_student = ""

# ✅ Initialize using infinity
highest = float("-inf")   # smaller than any score
lowest = float("inf")     # bigger than any score

for name, score in grades.items():
    print(f"{name}: {score}")

    if score > highest:
        highest = score
        highest_student = name

    if score < lowest:
        lowest = score
        lowest_student = name

print(f"Highest Score: {highest_student} ({highest})")
print(f"Lowest Score: {lowest_student} ({lowest})")
print(f"Class Average: {sum(grades.values()) / len(grades):.2f}")

```

## 🔍 Reflection

- What clicked:  

    - Getting better on understanding hw to manipulate data between list and dictionary.

- What confused me:  

    - Some functions for list and dictionary — I interchange them sometimes.
        - Like how storing data
            - List: 
                - list.append(var)
            - Dict:
                - dict[key] = value
                    - key: value
    - Pulling a data from a dict vs list
        - dict["Age"]
            - dict["key"]
        - list[0]
            - list[index]

- How I connected it to healthcare data:  

    These will be extremely used for data manipulation.

## 🎯 Next Step

    Maybe finally go back to BroCode's tutorial. Time stamp 2:17:44.
