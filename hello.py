from structures.lists import find_negative
if __name__ == '__structures__':
    # this file is provided for experimentation purposes
    # print('new dawn, new day')

    # discussion on errors
    # python is a dynamically typed language - what does that mean?
    # python has no 'primitive types' - why?

    # https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    #a = 5
    #b = 2
    #print(a / b)

    # floored quotient (aka: integer division)
    #print(a // b)

    # casting 'down'
    #print(int(a / b))

    # casting 'up'
    #print(float(int(a / b)))

    # booleans
    # if True == 1:
    #     print('here!')

    # if False == 0:
    #     print('also here!')

    # c = 2
    # d = 2.5
    # print('type of c: ' + str(type(c)))
    # print('type of d: ' + str(type(d)))

    # unicode character support
    # print('lie for you, die for you, paint the sky for you \U0001F304')

    # plot of Office Space (1999)
    # https://en.wikipedia.org/wiki/Pentium_FDIV_bug

    # define x
    #x = [1, 2, 3]

    # set y equal to x
    #y = x

    # copy everything from x over to z
    #z = x[:]

    # test equality (is) for x and y
    #if x is y:
     #   print('x (is) equal to y')
    #else:
     #   print('x (is) NOT equal to y')

    # test equality (is) for x and z
    
    # test equality (==) for x and z
    # if x == z:
    #   print('x is equal (==) to z')
    # else:
    #   print('x is NOT equal (==) to z')
    
    numbers = [-1, 5, 6, 7, 8]
    result = find_negative(numbers)
    print('result: ' + str(result))

    # numbers = [2, 3, 7, 8, 10]
    # result = even_only(numbers)
    # print('result: ' + str(result))

    # bonus
 # create a method "every other" which accepts an array(list)
 # of ints ans returns a new array returning only the original numbers of even positions.

class numbermanipulator:
    def every_other(numbers):
        return numbers[1::2] # Starting from index 1, skip every other element
    
    original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = every_other(original_array)
    print("original Array:", original_array)
    print("numbers at even positions:", result)