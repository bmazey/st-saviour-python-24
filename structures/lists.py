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
    # if the number in the list evens are module by 2 there are even
    # add even in the list with append function
    # return evens numbers of the list
    i = 0
    evens = []
    while i < len(numbers):
        if numbers [i] % 2 == 0:
            evens.append(numbers[i])
        i += 1
    return evens

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
    # % 10 result the last digit of the 4 digits numbers
    # add the last digit at the end of the list
    # return the new list
    i = 0
    leap = []
    while i < len(numbers):
        bag = numbers [i] % 10
        leap.append(bag)
        i += 1
    return leap

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
    # return the rounded number adding 1
    # add the rounded numbers to the star in lunar 
    # return star
    i = 0
    star = []
    while i < len(numbers):
        lunar = numbers[i] % 1
        if lunar >= 0.5:
            lunar = int(numbers[i]) + 1
        else:
            lunar = int(numbers[i])
        star.append(lunar)
        i += 1
    return star

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
    # the number if it is less than 0 return negative 
    i = 0   
    while i <  len(numbers):
        if numbers[i]< 0:
            return i 
        i += 1

    return -1


 # bonus
 # create a method "every other" which accepts an array(list)
 # of ints ans returns a new array returning only the original numbers of even positions.

class numbermanipulator:
    def every_other(self, numbers):
        return numbers[1::2]
