# 📅 2025/08/31

## 📝 Topic

1. List functions
    - list.append()
        - Adds a value in the list
    - list.count("")
        - Counts a specific value on the list
2. import random
    - random.shuffle(list)
        - Shuffles values inside a list
    - list.count("")
        - Counts specific values inside a list

## 💻 Code Example

```python
# 🎰 Slot Machine Exercise
# Instructions:
# 1. Start the player with a balance of 100.
# 2. Each spin costs 10.
# 3. The machine should randomly pick 3 symbols (ex: 🍒, 🍋, 🍇, 🔔).
# 4. If all 3 match → player wins 50.
#    If 2 match → player wins 20.
#    Otherwise → no win.
# 5. Keep playing until player quits (q) or runs out of money.

import random

balance = 100

symbols = ["🍒", "🍋", "🍇", "🔔"]
game = []

while True:
    if balance <= 0:
        print(f"Your balance is: {balance:.2f}")
        print("Exiting the game")
        break

    print(f"Your current balance: ${balance:.2f}")
    play = input("Do you want to play? $10 per game (y/n): ").lower()

    if play == "n":
        break

    balance -= 10
    game.clear()

    num1 = random.randint(0, 3)
    num2 = random.randint(0, 3)
    num3 = random.randint(0, 3)

    game.append(symbols[num1])
    game.append(symbols[num2])
    game.append(symbols[num3])

    print(game)

    if game.count("🍒") == 3 or game.count("🍋") == 3 or game.count("🍇") == 3 or game.count("🔔") == 3:
        balance += 50
        print(f"You Won $50 Balance: ${balance:,.2f}")
        continue
    elif game.count("🍒") == 2 or game.count("🍋") == 2 or game.count("🍇") == 2 or game.count("🔔") == 2:
        balance += 20
        print(f"You Won $20! Balance: ${balance:,.2f}")
    else:
        print(f"You Lose! Balance: ${balance:,.2f}")
```

## 🔍 Reflection

- What clicked:  

    I think I got a better understanding of loops, lists, dicts, and how to manipulate them.

- What confused me:  

    - I sometimes forget the actual syntax but I do know what needs to be done. 

- How I connected it to healthcare data:  

## 🎯 Next Step

    BroCode timestamp 4:05:44.

    I am interested on exploring IBM Data Engineering certificate.