#Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.


import random

# Ask the user for the number of dice to roll
num_dice = int(input("How many dice would you like to roll? "))

# Initialize a variable to store the sum of the dice rolls
total_sum = 0

# Roll each die and add the result to the total sum
for i in range(num_dice):
    roll = random.randint(1, 6)  # Roll a die (random number between 1 and 6)
    total_sum += roll

# Print the sum of all the dice rolls
print("The sum of the dice rolls is:", total_sum)
