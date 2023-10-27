def is_palindrome(word: str) -> bool:
    """
    is_palindrome accepts a string as input and returns ...
        - True if the provided word is a palindrome
        - False if the provided word is NOT a palindrome
    :param word: the input string provided by the user.
    :type word: str
    :returns: True or False depending on palindrome status
    :rtype: str
    """

    # start with a blank string to store the reverse of word
    reversed = ''

    # iterate over every character in word
    for character in word: 
        reversed = character + reversed 

    # check if reversed is equal to word
    return reversed == word
