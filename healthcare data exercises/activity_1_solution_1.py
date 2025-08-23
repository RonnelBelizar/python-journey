# Make a script for TB center:
# Seniors have discount for medication
# MTB: Proceed to center
# XDR: Consult doctor
# Print: If amenable for discount and/or next thing to do

patients = [
    {"name": "Nel", "age": 65, "diagnosis": "MTB"},
    {"name": "Doc", "age": 45, "diagnosis": "XDR"},
    {"name": "Shed", "age": 30, "diagnosis": "MTB"},
    {"name": "Bren", "age": 70, "diagnosis": "XDR"},
    {"name": "Joana", "age": 59, "diagnosis": "MTB"}
]

for patient in patients:

    name = patient["name"]
    age = patient["age"]
    diagnosis = patient["diagnosis"]

    discount_status = "Amenable for discount." if age >= 60 else "Not Amenable for discount."
    action = "Proceed to center." if diagnosis == "MTB" else "Consult Doctor."

    print(name, age, ": ", discount_status, action)
