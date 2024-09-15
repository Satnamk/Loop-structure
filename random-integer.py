#Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random

# Computer selects a random number between 1 and 10
number_to_guess = random.randint(1, 10)

# Infinite loop until the user guesses the correct number
while True:
    # Get user input
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is too high, too low, or correct
    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Correct! The number was:", number_to_guess)
        break  # End the game if the user guesses correctly