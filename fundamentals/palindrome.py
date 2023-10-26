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

    reversed = ""
   # i = 0
    #while i < len(word):
    for character in word:
        reversed = character + reversed
    return reversed == word
# were telling the comp. to take the word,reverse the letters and 
# if this word is the same as the original print the bolean answers

    #word = 'apple'

   # for character in word:
    #    print (character)

    #i = 0
    #while i < len(word):
    #    print ('value of i: ' + str(i) + 'character: ' + word[i])
    #    i += 1
