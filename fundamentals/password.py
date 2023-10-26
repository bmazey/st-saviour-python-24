
import random

def generate_password() -> str:
    import random
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
    #     
    password = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    symbol = '!@#$%^&*'
    # random_character = alphabet[n]
    #len(password) ==10

    for i in range(5) :
        l = random. randint(0, 25)
        password += alphabet[l]
    
    for i in range(4) :
        n = random. randint(0, 4)
        password += str(n)
    
    s = random.randint(0, 7)
    password += symbol[s]

    return password
