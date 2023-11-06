if __name__ == '__main__':
    # this file is provided for experimentation purposes
    print('new dawn, new day')
Oonly built in types
no primitive types in python
errors in python (3)
syntax error- python is telling us what we have written cannot be interpretted (error can be detectged before u run code)
runtime error looks good before( cannot be detected after u run the program or during the process of being run) ex (undefined variable, one off,dividing something by 0)
logical errors (the outcome you get isnt what you expect or it doesnt run even if its right and cant detect any errors.)

Next big topic: 
python infers the type of everything you write
python infers the type of thing that your writing
only has a few built in type ( integer,not a fraction or decimal. can be negative and 0)(float- Numbers with asomething after the decimal, has decimal percision)

a = 5
b = 2
print(a / b) - going to give us 2.5 (going to return a float)

floored quotient (aka: integer division)
print (a//b) - will give 2 because it needs to produce an integer

# casting 'down; - taking a type and converting it to another. taking a type with a higher form of persision and forcing it to a lower. ex talking a float and casting it down to an integer(2.5 to 5)
# print (int(a/b)) - forcing it to an integer, going to give us 2

casting 'up'
print(float(int(a/b))) - while casting up its converting from a lower form to a higher format
its going to give us a 2 but then converts back up to 2.0 becuase its still a int but forcing it up.

Golden rule of python - everything is an object 
