# bank_balance.py
import sys

# Check if 2 inputs are given (initial balance & deposit amount)
if len(sys.argv) == 3:
    print("User provided input values:")

    script_name = sys.argv[0]
    initial_balance = float(sys.argv[1])
    deposit_amount = float(sys.argv[2])

else:
    print("No input given - using default values:")

    script_name = sys.argv[0]
    initial_balance = 1000.0      # default initial balance
    deposit_amount = 500.0        # default deposit


# Calculate updated balance
updated_balance = initial_balance + deposit_amount

# Display output
print("Script Name:", script_name)
print("Initial Balance:", initial_balance)
print("Deposit Amount:", deposit_amount)
print("Updated Balance:", updated_balance)
