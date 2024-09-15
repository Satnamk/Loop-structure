# Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter
# the username and password again. This continues until the login information
# is correct or wrong credentials have been entered five times. If the information
# is correct, the program prints out Welcome. After five failed attempts the program
# prints out Access denied. The correct username is python and password rules.

# Set correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize attempt counter
attempts = 0

# Maximum allowed attempts
max_attempts = 5

# Loop to ask for username and password up to 5 times
while attempts < max_attempts:
    # Get input from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the input matches the correct credentials
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break  # Exit the loop when login is successful
    else:
        print("Incorrect username or password.")
        attempts += 1  # Increase the attempt counter

    # If 5 attempts are reached, deny access
    if attempts == max_attempts:
        print("Access denied.")
