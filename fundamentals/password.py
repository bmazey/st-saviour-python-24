
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
    #this is insane 
    #i = integer 
    #for statments --> loop 
    #for every integer in a range of 5, produce 5 letters from 0,25 (the alphabet). 
    #for every integer in a range of 4, produce 4 numbers from 0 to 9 
    # final case produces a random character of the 7 given     
    #returns all cases in one password 

    
    result = ''
    for i in range(5):
        l = random.randint(0, 25)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result += alphabet[l]

    for i in range(4):
        r = random.randint (0,9)
        result += str(r)
    
    character = '!@#$%^&*'
    c = random.randint(0,7)
    result += character[c]

    return result   
