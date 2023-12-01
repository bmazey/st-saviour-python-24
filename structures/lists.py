# Function to filter even numbers from a list
def evens_only(numbers: []) -> []:
    """
    evens_only() accepts a list of integers called "numbers" and returns a
    new list of integers which only contains the even members of the original
    list, preserving the initial order.
    """
    # Initialize an index variable
    i = 0
    evens = []
    
    # Iterate through the numbers list
    while i < len(numbers):
        # Check if the number is even
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])  # Add even number to the result list
        i += 1
    
    return evens

# Function to extract the last digit from four-digit integers in a list
def last_of_four_digits(numbers: []) -> []:
    """
    last_of_four_digits() takes a list of FOUR DIGIT INTEGERS ONLY [1000 - 9999]
    and returns a new list of integers which contains the final digit of the 
    original numbers, preserving the initial order.
    """
    # Initialize an index variable
    i = 0
    leap = []
    
    # Iterate through the numbers list
    while i < len(numbers):
        bag = numbers[i] % 10  # Extract the last digit
        leap.append(bag)  # Add the last digit to the result list
        i += 1
    
    return leap


# Function to round up decimal numbers in a list to the nearest integer
def round_up(numbers: []) -> []:
    """
    round_up() takes a list of DOUBLES and returns a new list of rounded INTEGERS.
    as a general rule, we only round up when the decimal is >= 5.
    """
    # Initializes an index variable
    i = 0
    boba = []
    
    # Iterates through the numbers list
    while i < len(numbers):
        bobao = numbers[i] % 1  # Get the decimal part of the number
        if bobao >= 0.5:
            bobao = int(numbers[i]) + 1  # Round up if decimal >= 0.5
        else:
            bobao = int(numbers[i])  # (Round down if decimal < 0.5)
        boba.append(bobao)  # Adds the rounded number to the result list
        i += 1
    
    return boba

# Function to find the position of the first negative number in a list
def find_negative(numbers: []) -> int:
    """
    find_negative() takes a list of integers and returns the position of the
    first occurrence of a negative number. If no such number exists, find_negative()
    should return -1.
    """
    # Initialize an index variable
    i = 0
    
    # Iterate through the numbers list
    while i < len(numbers):
        # Check if the number is negative
        if numbers[i] < 0:
            return i  # Returns the position of the first negative number
        i += 1
    
    return -1  # Return -1 if no negative number is found

# bonus
# create a method "every other" which accepts an array(list)
# of ints ans returns a new array returning only the original numbers of even positions.

def every_other(input_array):
    return input_array[::2] 

original_array = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_array = every_other(original_array)

print(result_array)

