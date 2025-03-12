# Prompt user for their age and membership status
age_str = input("Enter your age: ")
membership_str = input("Are you a member? (Yes/No): ")

# Convert age to an integer and normalize membership input
try:
    age = int(age_str)  # Convert age to integer
except ValueError:
    print("Invalid age input. Please enter an integer.")
    exit()  # Exit the program if the input is not a valid integer

membership = membership_str.strip().lower()  # Normalize membership input

# Nested if-else statements to check conditions
if age >= 18:
    if membership == "yes":
        print("Access granted.")
    else:
        print("Membership required for access.")
else:
    print("Access denied. Must be at least 18 years old.")
