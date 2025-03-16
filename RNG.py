# Imports
import secrets

# Metadata
AUTHOR = "Malcolm Allen"
VERSION = "5.2.3"

# Variables
numbers = list(range(10))
letters = list("abcdefghijklmnopqrstuvwxyz")
letNum = str(numbers + letters)
signs = ["+", "-"]
booleans = [True, False]

# Main function
def main():
    print(signRNG(secrets.choice(booleans), secrets.choice(range(1, 10)), secrets.choice(signs)))


# Functions
def signRNG(use_letters, num_digits, sign):
    """
    Generates a random value based on the sign and whether to use letters.
    """
    if sign == "-" and not use_letters:
        return -RNG(use_letters, num_digits)
    elif sign == "-" and use_letters:
        return "" + str(RNG(use_letters, num_digits))
    else:
        return RNG(use_letters, 5)

def RNG(use_letters, num_digits):
    """
    Generates a random string or number based on the use_letters flag.
    """
    if use_letters:
        return ''.join(secrets.choice(letNum) for _ in range(num_digits))
    else:
        return int(''.join(str(secrets.choice(numbers)) for _ in range(num_digits)))

# Run the main function
main()
