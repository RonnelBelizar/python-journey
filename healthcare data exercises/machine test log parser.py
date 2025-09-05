# Exercise: Machine Test Logs Parser

# You are given a list of test results from a diagnostic machine.
# Each result contains:
#   - sample_id → ID of the patient/sample
#   - test_type → TB, HIV, HCV, etc.
#   - result → Positive, Negative, Error
#   - date → date of test
#
# Tasks:
# 1. Count how many tests were run in total.
# 2. Count tests per test type (TB, HIV, HCV...).
# 3. Count how many results are Positive, Negative, and Error.
# 4. Find all tests that had errors.

# Sample data
test_results = [
    {"sample_id": "S001", "test_type": "TB",
        "result": "Positive", "date": "2025-09-01"},
    {"sample_id": "S002", "test_type": "TB",
        "result": "Negative", "date": "2025-09-01"},
    {"sample_id": "S003", "test_type": "HIV",
        "result": "Error", "date": "2025-09-02"},
    {"sample_id": "S004", "test_type": "HIV",
        "result": "Positive", "date": "2025-09-02"},
    {"sample_id": "S005", "test_type": "HCV",
        "result": "Negative", "date": "2025-09-03"},
]

total = len(test_results)
print(f"Total Tests: {total}")

tb = 0
hiv = 0
hcv = 0

tb_pos = 0
tb_neg = 0
hiv_pos = 0
hiv_neg = 0
hcv_pos = 0
hcv_neg = 0
errors = 0

for data in test_results:
    if data["test_type"] == "TB":
        tb += 1
        if data["result"] == "Positive":
            tb_pos += 1
        elif data["result"] == "Error":
            errors += 1
        else:
            tb_neg += 1
    elif data["test_type"] == "HIV":
        hiv += 1
        if data["result"] == "Positive":
            hiv_pos += 1
        elif data["result"] == "Error":
            errors += 1
        else:
            hiv_neg += 1
    elif data["test_type"] == "HCV":
        hcv += 1
        if data["result"] == "Positive":
            hcv_pos += 1
        elif data["result"] == "Error":
            errors += 1
        else:
            hcv_neg += 1


print(f"TB: {tb}, POS: {tb_pos}, NEG: {tb_neg}")
print(f"HIV: {hiv}, POS: {hiv_pos}, NEG: {hiv_neg}")
print(f"HCV: {hcv}, POS: {hcv_pos}, NEG: {hcv_neg}")
print(f"Errors: {errors}")
