"""lists in python: https://docs.python.org/3/tutorial/datastructures.html"""
def evens_only(numbers: []) -> []:
    """
    evens_only() accepts a list of integers called "numbers" and returns a
    new list of integers which only contains the even members of the original
    list, preserving the initial order.
    for example [3, 7, 12, 4, 13, 0] -> [12, 4, 0]
    :param numbers: the original list of integers
    :type numbers: []
    :returns: a new list of only even integers 
    :rtype: []
    """
    # TODO implement evens_only()
    i = 0 
    evens = []
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
        i += 1
    return evens

#if the numbers in the list "evens" are even(divisible by 2, %2), add the even number to the end of the list

def last_of_four_digits(numbers: []) -> []:
    """
    last_of_four_digits() takes a list of FOUR DIGIT INTEGERS ONLY [1000 - 9999]
    and returns a new list of integers which contains the final digit of the 
    original numbers, preserving the initial order.
    for example [1004, 9181, 1700, 4565] -> [4, 1, 0, 5]
    :param numbers: the original list of four digit integers
    :type numbers: []
    :returns: a new list of last digits only
    :rtype: []
    """
    # TODO implement last_of_four_digits()
    i = 0
    bean = []
    while  i < len(numbers):
        bag = numbers[i] % 10
        #modulo 10 results in the last digit of the 4 digit number 
        bean.append(bag)
        #add the last digit( % 10) to the end of the list
        i += 1
    return bean
#return the list 


def round_up(numbers: []) -> []:
    """
    round_up() takes a list of DOUBLES and returns a new list of rounded INTEGERS.
    as a general rule, we only round up when the decimal is >= 5.
    for example [1.2, 3.6, 7.9, 4.1] -> [1, 4, 8, 4]
    :param numbers: the original list of doubles
    :type numbers: []
    :returns: a new list of rounded integers
    :rtype: []
    """
    # TODO implement round_up()
    i = 0 
    beeb = []
    while i < len(numbers):
        beebo = numbers[i] % 1
        if beebo >= 0.5:
            beebo = int(numbers[i]) + 1
        else:
            beebo = int(numbers[i])
        beeb.append(beebo)
        i += 1
    return beeb

def find_negative(numbers: []) -> int:
    """
    find_negative() takes a list of integers and returns the position of the
    first occurence of a negative number. if no such number exists find_negative()
    should return -1.
    for example: [0, 4, -2, 17] -> 2
    :param numbers: the original list of integers
    :type numbers: []
    :returns: the position of the first negative integer or -1 if no such integer exists
    :rtype: int
    """
    # TODO implement find_negative()
    i = 0 
    while i < len(numbers):
        if numbers [i] < 0:
            return i
        i += 1
    return -1
