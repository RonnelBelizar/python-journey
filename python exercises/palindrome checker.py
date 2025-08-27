# Problem 2: Palindrome Check

# Write a function that checks if a string is a palindrome.

# A palindrome is a word that reads the same backward as forward.

# Ignore capitalization.

word = input("Enter Word: ")

while word.lower() != "exit":

    print("Palindrome") if word[::].lower(
    ) == word[::-1].lower() else print("Not palindrome")
    word = input("Enter Word: ")
