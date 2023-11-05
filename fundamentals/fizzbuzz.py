def fizzbuzz(number: int) -> str:
    """
    fizzbuzz is a function which takes a number and returns ...
        - 'fizz' if the number is a multiple of 3
        - 'buzz' if the number is a multiple of 5
        - 'fizzbuzz' if the number is a multiple of 3 and 5
        - an empty string if the number is not a multiple of 3 or 5

    :param number: the input integer provided by the user.
    :type number: int
    :returns: a string with some combination of 'fizz' and 'buzz' 
    :rtype: str
    """
    result = ''

    # check if multiple of 3
    if number % 3 == 0:
        result += 'fizz'

    # check if multiple of 5
    if number % 5 == 0:
        result += 'buzz'

    return result
