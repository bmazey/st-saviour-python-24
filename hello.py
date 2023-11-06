if __name__ == '__main__':
    # this file is provided for experimentation purposes
    print('new dawn, new day')

from fundamentals.password import generate_password

generate_password()

a = 5
b = 2

print(float(int(a/b)))
print(a/b)

c = 2
d = 2.5
print('type of c: ' + str(type(c)))
print('type of d: ' + str(type(d)))
print('lie for you, die for you, paint the sky for you \U0001F304')
print('YEEEEEHAW \U0001F920')
print('\U0001F648 ...Thanks!')

#define x
x = [1, 2, 3]
#set x and y equal to each other
y = x
#bring everything from x over to z
z = x[:] 
#test equality (x and y)
if x is y:
    print('x (is) equal to y')
else:
    print(' x (is) NOT equal to y')
 #test equality (z and x)
if x is z:
    print('x (is) equal to z')
else:
    print(' x (is) NOT equal to z')

#test equality (==)
if x == z:
    print('x is equal (==) to z')
else:
    print(' x is NOT equal (==) to z')
