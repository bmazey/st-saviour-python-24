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
    symbol = '!@#$%^&*'

#pull 5 random letters and add to password
    for i in range(5):
        l = random.randint(0, 25)
        password += alphabet[l]

#pull 4 random letters and add to password
    for i in range(4):
        n = random.randint(0, 9)
        password += str(n)

#pull random symbol
    s = random.randint(0, 7)
    password += symbol[s]

    return password 
   
