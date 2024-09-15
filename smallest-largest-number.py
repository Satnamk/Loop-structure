# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.

def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            number = float(user_input)  # Convert to float to handle decimal numbers
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    if numbers:
        print(f"The smallest number is: {min(numbers)}")
        print(f"The largest number is: {max(numbers)}")
    else:
        print("No numbers were entered.")

# Call the function
find_min_max()
