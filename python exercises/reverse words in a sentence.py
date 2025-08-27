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
