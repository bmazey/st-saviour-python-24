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
    r = random.randint(0, 25)

    print('random number: ' + str(r))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print('random letter: ' + alphabet[r])

    r = random.randint(0, 25)
    print('new random number: ' + str(r))

    return ''
