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
    i = 0
     # make an empty list (this was annoying hense the name stupid) to have things added to the end
    stupid = []
     # While the length of our given numbers are greater than 0, take the first term and test if it modulo 2 equals 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            # if the number modulo 2 equals 0 add it to our list
            stupid.append(numbers[i])
        # move onto the next term in the list
        i += 1
        
        # print the numbers that pass the test in a list
    return stupid

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
    i = 0
    # make an empty list
    four = []
    # While the length of our given numbers are greater than 0, modulo all the numbers in the list by 10 to get the last digit, then ass it to the list
    while i < len(numbers):
        annoy = numbers[i] % 10
        four.append(annoy)
        # test the next object in the list
        i += 1
        # return the newly created list
    return four

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
    i = 0 
    # make an empty list
    boop = []
    # While the length of our given numbers are greater than 0, modulo all the numbers in the list by 1, if you get a number less than .5 drop the decimal and return the  number, if you get a number greater than or equal to .5 then you drop the decimal point and add 1 to the number
    while i < len(numbers):
        decimal = numbers[i] % 1
        if decimal >= .5:
            decimal = int(numbers[i]) + 1
        else:
            decimal = int(numbers[i])
        boop.append(decimal)
        # test the next object in the list
        i += 1
    # return the newly created list
    return boop

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
    i = 0
    # saying while i is less then the length of the list 'numbers' and if the first is less than 0 then we print it
    while i < len(numbers):
        # print('i value: ' + str(i) + 'number value: ' + str(numbers[i]))
        if numbers[i] < 0:
            return i
        # we are telling the code that after it returns the number if it is less than 0 we are telling the coed to test the next number in the list
        i += 1

    return -1

def every_other(numbers: []) -> []:
    """
    create a method 'every other' 
    it accepts an array (list) of ints
    and returns a new array containing ONLY 
    the origional numbers with even positions
    """
    i = 0
    while i < len(numbers):
        if numbers[i].index % 2:
            return numbers
        i += 1
    
    return 