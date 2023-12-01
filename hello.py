# this file is provided for experimentation purposes
# bonus
# create a method "every other" which accepts an array(list)
# of ints ans returns a new array returning only the original numbers of even positions.

def every_other(input_array):
    return input_array[::2] 

original_array = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_array = every_other(original_array)

print(result_array)
