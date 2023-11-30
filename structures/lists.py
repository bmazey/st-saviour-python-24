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
            # if the numbers within the list evens are modulo 2 they are even
            evens.append(numbers[i])
            # apends evens into a list 
        i += 1
    return evens
# returning even numbers of the list
# if the numbers in the list "evens" are even(divisible by 2, %2), add the even number to the end of the list

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
        # modulo 10 results in the last digit of the 4 digit number 
        bean.append(bag)
        # add the last digit( % 10) to the end of the list
        i += 1
    return bean
# return the list 


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
    # beeb is an open list 
    while i < len(numbers):
        beebo = numbers[i] % 1
        # returning the same number 
        if beebo >= 0.5:
            beebo = int(numbers[i]) + 1
            # returns the rounded number (int) adding 1 to produce the number rounded up
        else:
            beebo = int(numbers[i])
        beeb.append(beebo)
        # appends the rounded numbers in beebo to the list beeb
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
            #if the numbers in the list of i are less that zero (negative) return the negative 
            return i
        i += 1
    return -1
# return the negative one if there is no negative 

def every_other(numbers: []) -> int:
    """
    every_other accepts a list of int and returns 
    every other object in the list 
    example [2, 4, 8, 16, 32, 64, 128] -> 4, 16, 64

    """
    # TODO implement every_other

    other_value = []
# index returns position of a specified value 

    for index in range(0, len(numbers), 2):
# For each position (index) in a range beginning at 0 and skipping to 2 in the list
# Considering the index 2 as 1
    
        other_value.append(numbers[index])
# Append the value after the skipped index (0, skip, 1, skip, 2)

    return other_value

