# 📝 Exercise: Student Gradebook System

# Write a Python program that acts as a mini gradebook for a class.

# Requirements:
# Ask the user how many students are in the class.
# For each student:
# Ask for the student’s name.
# Ask how many subjects they have.
# For each subject, ask for the subject name and grade (0–100).
# Store the subjects and grades in a dictionary for that student.
# Store all students in a list of dictionaries, something like:

# [
#   {"name": "Alice", "grades": {"Math": 95, "English": 88}},
#   {"name": "Bob", "grades": {"Science": 76, "History": 82}}
# ]

# After all students are entered, display a summary report:

# Each student’s name
# Their average grade (using a function you write)
# Whether they passed or failed (≥ 75 = Pass, else Fail)

records = {}

number_students = int(input("Number of students: "))
for num in range(number_students):
    name = input("Enter Name: ")
    number_subjects = int(input("How many subjects: "))
    grades = {}
    for num in range(number_subjects):
        subject = input("Subject name: ")
        grade = int(input("Subject grade: "))
        grades[subject] = grade
    records[name] = grades

print(records)
# {'nel': {'math': 65, 'physics': 60}, 'joana': {'math': 99, 'physics': 100}}

print("---SUMMARY REPORT---")

for name, grades in records.items():
    ave = (data["math"] + data["physics"]) // 2

    def status():
        if ave >= 75:
            print("Pass")
        else:
            print("Fail")

    print("Names: ", data["name"], "Ave Grade: ", ave, "|", status())
