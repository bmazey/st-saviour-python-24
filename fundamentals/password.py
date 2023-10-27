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
    # start with a blank string to add the reverse of password
    password = ''
    # defining the password character complexity requirements
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    symbol = '!@#$%^&*' 
    # random_character = alphabet[n]
    #len (password) ==10
    # setting the range of alphabet
    for i in range (5):
        n = random.randint(0,25)
        password += alphabet[n]
    
    # setting the range of the string
    for i in range (4):
        n = random.randint(0, 9)
        password += str(n)
    # setting the range of the symbols
    s = random.randint(0,7)
    password += symbol[s]
    # returning the result of password
    return password

