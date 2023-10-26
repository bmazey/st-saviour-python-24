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
    #reversed is variable for empty str
    #for every character in a word (str bool), take that character and reverse it 
    #code produces a bool if the returned reversed word is a palindrome or not

    reversed = ""
    for character in word:
        reversed = character + reversed 
    return reversed == word