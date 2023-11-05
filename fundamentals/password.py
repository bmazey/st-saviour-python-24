import random

def generate_password() -> str:
    """
    generate_password takes no arguments and produces a string
    which meets the following password complexity requirements:
        - the length of the password is 10
        - the first 5 characters are lower case letters
        - the next 4 characters are digits [0-9]
        - the final character is a symbol [!@#$%^&*]
        - it's relatively uncommon to generate the same password twice 
    """
    password = ''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*'

    # add 5 random letters
    for i in range(5):
        password += alphabet[random.randint(0, len(alphabet) - 1)]

    # add 4 random digits
    for i in range(4):
        password += digits[random.randint(0, len(digits) - 1)]

    # add a random symbol
    password += symbols[random.randint(0, len(symbols) - 1)]

    return password
