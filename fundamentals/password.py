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
    
#pull 5 letters from variable(alphabet)
# associate each letter with a random integer
    for i in range(5):
        l = random.randint(0, 25)
        password += alphabet[l]

#pull 4 integers by using random function, only pull digits
# must convert to string using str(variable_name)    
    for i in range(4):
        n = random.randint(0, 9)
        password += str(n)
    
#pull a random symbol from variable(symbol)
#no need for loop since only pulling 1
#use of lists
    s = random.randint(0, 7)
    password += symbol[s]
    
    return password
    

    

    
    

