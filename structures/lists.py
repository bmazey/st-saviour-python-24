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
    evens = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
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
    # TODO implement last_of_four_digits()
    return []
remainder = []
i = 0
while i < len(last_of_four_digits): 
    if last_of_four_digits % 10 == [1,2,3,4,5,6,7,8,9]:
        remainder.append(numbers[i])
        i += 1
return remainder

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
    return []

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
        #print('i value: ' + str(i) + 'number value: ' + str(numbers[i]))
        if numbers[i] < 0:
            return i
        i += 1
   
    return -1
