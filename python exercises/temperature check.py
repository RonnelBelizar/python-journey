# Loops

# Write a program that prints numbers from 1 to 20 but:
# Skip numbers that are multiples of 3.
# Stop completely if the number reaches 17.

for num in range(1, 21):
    if num == 17:
        break

    if num % 3 != 0:
        print("", num)
