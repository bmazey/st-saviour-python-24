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
    # TODO implement our fizzbuzz function ...

 #if a number (int) can be divided into a number without remainder (% modulo) it outputs a result (empty str)
 # if % of 3 --> fizz 
 # if % of 5 --> buzz
 #result is either fizz, buzz, or fizzbuz

    result = ''
    if number % 3 == 0:
        result += "fizz"
    if number % 5 == 0:
        result += "buzz"
    return result 
        