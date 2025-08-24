# 🏥 Problem: TB Clinic Daily Log

# You are working at a TB diagnostic center.

# Every day, patients come in for testing. For each patient, you record:

# Name
# Age
# Diagnosis → either "MTB" (Tuberculosis detected) or "XDR" (Drug-resistant TB)
# Payment Type → "Cash" or "Insurance"

# Your task:

# Write a program that:
# Lets the user enter 5 patient records (name, age, diagnosis, payment).
# Stores them in a list of dictionaries.

# After input, prints a report:

# Total patients.
# Number of MTB and XDR cases.
# Number of seniors (age ≥ 60).
# How many paid in cash vs. insurance.

name_counter = 0
mtb_counter = 0
xdr_counter = 0
senior_num = 0
cash = 0
insurance = 0

patient_data = []


while True:

    if name_counter != 5:
        name_counter += 1
    else:
        break

    name = input("Enter patient name: ")
    age = input("Enter age: ")
    diagnosis = input("Enter diagnosis (MTB/XDR): ")
    payment = input("Enter payment (Cash or Insurance): ")

    patient = {
        "name": name.title(),
        "age": int(age),
        "diagnosis": diagnosis.upper(),
        "payment": payment.title(),
    }

    patient_data.append(patient)

print("Total patients: ", name_counter)

for record in patient_data:
    if record["diagnosis"] == "MTB":
        mtb_counter += 1
    else:
        xdr_counter += 1

    if record["age"] >= 60:
        senior_num += 1

    if record["payment"] == "Cash":
        cash += 1
    else:
        insurance += 1

print("--- Summary ---")
print("Total patients: ", name_counter)
print("MTB patients: ", mtb_counter)
print("XDR patients: ", xdr_counter)
print("Number of seniors: ", senior_num)
print("Cash payments: ", cash)
print("Insurnace payments: ", insurance)
