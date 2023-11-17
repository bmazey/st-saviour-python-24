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
    #create an open string
    evens = []
    i = 0
    #establish a while loop to test all elements of the test list
    while i < len(numbers):
    #if the element in the test list is divisible by 2, it should be added to the open list
        if numbers[i] % 2 == 0: 
            evens.append(numbers[i])
        i += 1
    #return the originally empty list with the the even values in numbers.        
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
    #Create open list to return
    #Use of while loop to test every element in list
    i = 0
    four = []
    while i < len(numbers):
    #Any element mod 10 in the numbers list will return the last digit of a 4 digit integer
        num = numbers[i] % 10
    #add that last didgit of each integer to the returned list
        four.append(num)
        i += 1
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
    # TODO implement round_up()
    #create open list which will be returned
    i = 0
    rounded = []
    #Create while loop to analyze each value in numbers list
    while i < len(numbers):
        decimal = numbers[i] % 1
    #If each value mod 1 is equal or higher than 0.5, round up (by adding 1)
        if decimal >= 0.5:
         decimal = int(numbers[i]) + 1
    #If the value mod 1 is equal to less that 0.5, round down (by converting to int)
        else:
         decimal = int(numbers[i])
        rounded.append(decimal)
        i += 1

    return rounded


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
    #numbers are negatve if equal to less that zero
    #i is an integer representing the index placement of each number in the list
    i = 0 
    while i < len(numbers):
            numbers[i]
            if numbers[i] < 0:
    #return each value of i that has a corresponding integer in the list less than 0
                return i 
            i += 1
    #If there are no negatives, return -1 
    return -1
    
def every_other(numbers: []) -> []:
    #Define that each every_other accepts a list (numbers) and returns a list
    """
    every_other() accepts a list of integers and returns a new list containing 
    only the original numbers with even positions
    """
    # TODO implement every_other()
    #create open list that i going to be returned
    evens = []
    #insert a slice to define every other integer in numbers into a variable
    slice = numbers[::2]
    #add these integers to the new list
    evens.append(slice)
    #return the list
    return evens
        
            
    