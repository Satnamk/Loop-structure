# Write a program that asks the user to enter numbers until they input an empty
# string to quit. At the end, the program prints out the five greatest numbers
# sorted in descending order. Hint: You can reverse the order of sorted list
# items by using the sort method with the reverse=True argument.

# Initialize an empty list to store the numbers
numbers = []

# Keep asking for input until the user enters an empty string
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the input is empty (the user wants to quit)
    if user_input == "":
        break

    # Convert the input to a number and add it to the list
    try:
        number = float(user_input)  # Accept both integers and floats
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Sort the numbers in descending order and print the top 5
numbers.sort(reverse=True)
top_five = numbers[:5]

# Output the result
print("The five greatest numbers are:", top_five)
