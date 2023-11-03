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
    #create variable for alphabet
    for i in range(5):
        x = random.randint(0,25)
        password += alphabet[x]
        
    for i in range(4):   
        y= random.randint(0,9)
        password += str(y)
    
    symbol = '!@#$%^&*'
    for i in range(1):
        z = random.randint(0,7)
        password += symbol [z]
    return password
