# Lists & Loops

# Tasks:

# Remove duplicates → result should be [2, 4, 6, 8, 10].
# Find the largest number without using max().

numbers = [2, 4, 6, 2, 8, 4, 10]

cleaned_numbers = []

for num in numbers:
    if num not in cleaned_numbers:
        cleaned_numbers.append(num)

print(cleaned_numbers)
