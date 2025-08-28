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
