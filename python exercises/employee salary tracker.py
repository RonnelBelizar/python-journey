# 📝 Exercise: Employee Salary Tracker
# Requirements:

# Ask how many employees to add.
# For each employee, ask for:
# Employee name (string)
# Salary (float)

# Store them in a dictionary like:

# {"John": 35000.0, "Maria": 42000.0, "Alex": 38000.0}

# After input, display:

# Each employee with their salary.
# The highest salary and who earns it.
# The lowest salary and who earns it.
# The total payroll (sum of all salaries).
# The average salary.

num_employee = int(input("How many employees?: "))

records = {}
for _ in range(num_employee):
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    records[name] = salary

high = float("-inf")
low = float("inf")

high_name = ""
low_name = ""

for name, salary in records.items():
    if salary > high:
        high = salary
        high_name = name

    if salary < low:
        low = salary
        low_name = name

print("---SUMMARY---")

print(f"Highest Earner: {high_name}: {high:,.2f}")
print(f"Lowest Earner: {low_name}: {low:,.2f}")
print(f"Total Payroll: {(sum(records.values())):,.2f}")
ave = sum(records.values()) / len(records.values())

print(f"Average Salary: {ave:,.2f}")
