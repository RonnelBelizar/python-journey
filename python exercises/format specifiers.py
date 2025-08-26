# 🏦 Bank Interest Exercise
#
# Write a Python program that:
# 1. Asks the user for:
#    - Initial deposit (P)
#    - Annual interest rate (in %, convert to decimal)
#    - Number of times interest is compounded per year (n)
#    - Number of years (t)
#
# 2. Use the compound interest formula:
#       A = P * (1 + r/n) ** (n * t)
#       I = A - P
#
#    Where:
#       A = Final amount (principal + interest)
#       I = Interest earned
#
# 3. Print out the final amount and the total interest earned.


initial_deposit = float(input("Enter initial deposit: "))
interest_rate = float(input("Enter interest rate in %: "))
interest_rate_dec = interest_rate / 100
num_interest = int(
    input("Enter number of times interest is compounded per year: "))
years = int(input("Enter number of years: "))

final_amount = initial_deposit * \
    pow((1 + interest_rate_dec/num_interest), num_interest * years)
int_earned = final_amount - initial_deposit

print(f"Final amount: P{final_amount:>,.2f}")
print(f"Interest earned: P{int_earned:>+,.2f}")
