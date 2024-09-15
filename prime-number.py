# Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result
# is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

# Ask the user for an integer
num = int(input("Enter an integer: "))

# Assume the number is prime
is_prime = True

# Prime numbers must be greater than 1
if num <= 1:
    is_prime = False
else:
    # Check for divisibility by numbers from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Print the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
