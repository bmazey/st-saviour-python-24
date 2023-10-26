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
    # TODO - implement our is_palindrome function ...
    
    #open empty string to build on
    reversed = ''

    #build a for loop
    for character in word:
        reversed = character + reversed
        
    #returns a boolean
    return word == reversed
