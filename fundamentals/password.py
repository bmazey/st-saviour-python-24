
import random
from xml.dom.pulldom import CHARACTERS
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
    
    result = ''
    for i in range(5):
        l = random.randint(0, 25)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result += alphabet[l]

    for i in range(4):
        r = random.randint (0,9)
        result += str(r)
    
    character = '!@#$%^&*'
    c = random.randint(0,8)
    result += character[c]

    return result   
