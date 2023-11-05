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
    # check if word is equal to reverse (using slicing)
    return word == word[::-1]
