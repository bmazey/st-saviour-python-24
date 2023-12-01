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
    # making a list for the even numbers to go in
    evens = []
    # sets variable i to first position in the list
    i = 0
    # stating that i is less than the length of numbers shows that i represents a position inside the list
    while i < len(numbers):
    # mod 2 because only even numbers are divisible by 2 and have no remainder
        if numbers[i] % 2 == 0:
    # adds those numbers to the list of evens
            evens.append(numbers[i])
    # move to the next position
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
    # list for remainders
    remainder = []
    # set to first position in list
    i = 0
    # i is a position inside the list
    while i < len(numbers): 
    # mod 10 to get the remainder that is in the ones place of the number
    # also appending that to the list of remainders
        remainder.append(numbers[i] % 10) 
    # move to next position
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
    # list for rounded numbers
    round = []
    # first position in list
    i = 0 
    # while loop states that the position is less then the length of the numbers list
    while i < len(numbers):
    # numbers mod 1 because all whole numbers are divisible by 1, so the remainder would be the decimal
    # if statement for if the remainder is greater than 0.5
        if numbers[i] % 1 >= 0.5:
    # makes that number an integer which removes the decimal value
    # adds 1 because that would be equivalent of rounding up to the next number
            x = int(numbers[i]) + 1
    # appends the variable for the rounded number 
            round.append(x)
    # else statement for numbers that
        else: 
            y = int(numbers[i])
            round.append(y)
        i += 1
    return round

    
    



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
