if __name__ == '__main__':
    # this file is provided for experimentation purposes
    # print('new dawn, new day')

    # discussion on errors
    # python is a dynamically typed language - what does that mean?
    # python has no 'primitive types' - why?

    # https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    a = 5
    b = 2
    print(a / b)

    # floored quotient (aka: integer division)
    print(a // b)

    # casting 'down'
    print(int(a / b))

    # casting 'up'
    print(float(int(a / b)))

    # booleans
    if True == 1:
        print('here!')

    if False == 0:
        print('also here!')

    c = 2
    d = 2.5
    print('type of c: ' + str(type(c)))
    print('type of d: ' + str(type(d)))

    # unicode character support
    print('lie for you, die for you, paint the sky for you \U0001F304')

    # plot of Office Space (1999)
    # https://en.wikipedia.org/wiki/Pentium_FDIV_bug



