# Temperature Check:
# Write a program that asks the user for the temperature in Celsius, then:

# If temp > 30 → print "It's a hot day"
# If 20 <= temp <= 30 → print "It's a nice day"
# If 10 <= temp < 20 → print "It's a bit cold"
# Else → print "It's freezing!"

temp = int(input("Enter Temperature: "))

if temp > 30:
    print("It's a hot day")
elif 20 <= temp <= 30:
    print("It's a nice day")
elif 10 <= temp < 20:
    print("It's a bit cold")
else:
    print("It's freezing!")
