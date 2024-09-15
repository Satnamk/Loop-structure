# Write a program that asks the user to enter the names of five cities one by on
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input. Use a for loop for asking the names and
# a for/in loop to iterate through the list.

# Initialize an empty list to store city names
cities = []

# Use a for loop to ask the user for five city names
for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

# Print the cities one by one in the same order
print("\nThe cities you entered are:")
for city in cities:
    print(city)
