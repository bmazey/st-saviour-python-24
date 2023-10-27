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

    # start with a blank string to add the reverse of the number
    result = '' 
    # checking if it's a multiple of three
    if number % 3 == 0:
        result += 'fizz'
    # checking if it's a multiple of five
    if number % 5 == 0:
        result += 'buzz'
    # returning the result of the number
    return result
      

