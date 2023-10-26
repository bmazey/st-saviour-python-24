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
    # TODO - implement generate_password ...
    password = ''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    mickey = '!@#$%^&*'

    # do this five times ...
    for i in range(5):
        a = random.randint(0, 25)
        # were telling the comp. to take random letters from the alphabet and print it after each other 5 times
        password += alphabet[a]
    
    for i in range(4):
        n = random.randint(0, 9)
        # were telling the comp. to take random numbers and print them 4 times after each other
        password += str(n)
     
    c = random.randint(0, 7)
    # were telling the comp. to choose a random character from the list and print it once after the numbers
    password += mickey[c]

    return password
        
 