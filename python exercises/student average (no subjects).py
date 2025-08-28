# 📝 Easier Exercise: Student Average (No Subjects)
# Requirements:

# Ask the user for a student’s name.
# Ask how many grades they want to enter.
# Collect the grades in a list.
# Compute the average.
# Print the student’s name, grades, average, and whether they passed (≥ 75).

name = input("Enter a name: ")
grade_num = int(input("How many grades: "))

grades = []

for num in range(grade_num):
    grade = int(input("Enter grade: "))
    grades.append(grade)

average = sum(grades) / len(grades)
result = ""

if average >= 75:
    result = "Passed"
else:
    result = "Failed"

print(f"Name: {name}, Average = {average}, Status: {result}")
