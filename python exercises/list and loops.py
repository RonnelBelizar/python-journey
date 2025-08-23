# Lists & Loops

# Tasks:

# Remove duplicates → result should be [2, 4, 6, 8, 10].
# Find the largest number without using max().

name = ["nel", "doc", "shed", "bren", "nel", "shed"]

cleaned_names = []

for item in name:
    if item not in cleaned_names:
        cleaned_names.append(item)

print(cleaned_names)
