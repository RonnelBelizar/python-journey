# Guessing Game

# The secret number is 7.
# The user has 3 tries maximum to guess the number.
# If the user guesses correctly → print "You won!" and stop the game.
# If the user fails after 3 attempts → print "Sorry, you lost."


num = int(input("Enter a number: "))

counter = 0

for i in range(1):
    if num != 7:
        counter = 1 + i
    elif counter == 3:
        print("You lost")
    else:
        print("You won")
