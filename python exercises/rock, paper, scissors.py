# Rock, Paper, Scissors

import random

options = ("rock", "paper", "scissors")


while True:

    player = input("Enter a choice (q to quit): ")

    if player == "q":
        print("Thank you for playing!")
        break

    if player not in options:
        print("Invalid input")
        continue

    computer = random.choice(options)

    def answers():
        print(f"Player: {player}")
        print(f"Computer: {computer}")

    if player == computer:
        answers()
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        answers()
        print("You win!")
    elif player == "paper" and computer == "rock":
        answers()
        print("You win!")
    elif player == "scissors" and computer == "paper":
        answers()
        print("You win!")
    else:
        answers()
        print("You Lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again == "n":
        print("Thank you for playing!")
        break
