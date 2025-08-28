# 📝 Exercise: Patient Health Summary

# Requirements:
# Print each patient with their details.
# Find the patient with the highest cholesterol.
# Find the patient with the lowest blood pressure.
# Calculate the average age of all patients.

patients = {
    "Alice": {"Age": 32, "Blood Pressure": 120, "Cholesterol": 190},
    "Bob": {"Age": 45, "Blood Pressure": 135, "Cholesterol": 210},
    "Charlie": {"Age": 29, "Blood Pressure": 110, "Cholesterol": 180},
    "Diana": {"Age": 50, "Blood Pressure": 145, "Cholesterol": 240},
}

highest = float("-inf")
lowest = float("inf")
highest_patient = 0
lowest_patient = 0
total_age = 0
for name, data in patients.items():
    print("Name: ", name, data)

    if data["Cholesterol"] > highest:
        highest = data["Cholesterol"]
        highest_patient = name

    if data["Cholesterol"] < lowest:
        lowest = data["Cholesterol"]
        lowest_patient = name

    total_age += data["Age"]

ave = total_age/len(patients)

print(f"Highest in Cholesterol: {highest_patient}, {highest}")
print(f"Lowest in Cholesterol: {lowest_patient}, {lowest}")


print(f"Average Age = {ave}")
