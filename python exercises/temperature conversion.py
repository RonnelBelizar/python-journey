# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must no contain digits

while True:

    user = input("Enter username: ")

    if user == "exit":
        break

    def rule():
        print("""
            1. username is no more than 12 characters
            2. username must not contain spaces
            3. username must not contain digits
            """)

    rule() if len(user) > 12 or " " in user or not user.isalpha() else print("Granted!")
