if __name__ == '__main__':
    # this file is provided for experimentation purposes

#floating point precision: precise numerical data after the decimal 

#EVERYTHING IN PYTHON IS AN OBJECT. NOTHING IS PRIMITIVE 

#division
    a = 5 
    b = 2
    print (a/b)

#floored quotient (integer division)
    print (a//b)

#casting 'down"
    print (int(a/b))
#losing floating point precision

#casting 'up'
    print(float(int(a/b)))
#prints 2.5
#int casts answer down into 2
#float turns answer into 2.0
#convert integer 2 into a float --> 2.0

c = 2
print('type of c: ' + str(type(c)))
d = 2.5 
print('type of d: ' + str(type(d)))
#python being dynamically typed does not mean that there is no type system 

#unicode character support --> emojis 
print('lie for you, die for you, paint the sky for you \U0001F304')
#thats crazy

""""
'and' (&&) both variables a and b must be true for the entire statement 'a and b' to be true 
'or' (II) only one variable needs to be true for the entire statement to be true in the statement 'a or b'
***'xor' (+) its own inverse 'the heart of cryptography' encrypts data 
***no xor operator in python, must compute xor 
not (!)
equals (==)
"""

#1, 2, 3 is a list in x 
x = [1, 2, 3]

#make y equal x
y = x

#using slice, copy everything from x to z
z = x[:]

#testing equality using 'is'
if x is z:
    print('x IS equal to z')
else:
    print('x is NOT equal to z')
#x and z are not the same, z has all copied information from x
#z is only a copy of all things in x, they are not the same object like x and y

if x is y:
    print('x IS equal to y')
else:
    print('x is NOT equal to y')

#test equality for x and z (==)
if x == z:
    print('x is EQUAL to z')
else: 
    print('x is NOT EQUAL to z')