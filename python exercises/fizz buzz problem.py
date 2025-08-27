# Problem 1: FizzBuzz

# Write a program that prints numbers from 1 to 100.

# For numbers that are multiples of 3, print "Fizz" instead of the number.

# For numbers that are multiples of 5, print "Buzz".

# For numbers that are multiples of both 3 and 5, print "FizzBuzz".

for num in range(1, 101):

    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num != 0:
        print(num)
