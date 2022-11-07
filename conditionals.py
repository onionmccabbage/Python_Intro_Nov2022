# we can carry put conditional logic
s = 'text' # this is a string
s = 4 # now it points to an integer
s = (3,) # a tuple
s = 4.2  # a float
if type(s) == str: # check the data type
    print('it is a string')
elif type(s) == int: # elif means 'else if'
    print(' it is an integer')
elif type(s) == float:
    print('it is a float')
else:
    print('not a string or an integer or float')

# we can type-check fresh data
n = input('Please enter an integer numeric value ')
# check if it's a numeric (i.e. digits only)
if n.isnumeric():
    print('You entered', int(float(n)) ) # confidently type cast as in of float (from string)
    n = int(float(n)) # safely cast to an integer
else:
    print('that is not numeric')

squares = {1, 4, 9, 16, 25}
primes  = (1, 2, 3, 5, 7, 11)

# we can do other checks
if n/2 == n//2 and n in squares: # check if it is an even number and a square nubmer
    print('that is an even square number')
elif n/2 != n//2 or n in primes: # check odd or prime
    print('that is an odd or prime number')

# comparison operators
# ==, !=, <, >, <=, >=

# the 'while' loop
while True:
    print('this will never end')
    a = input('is it lunch yet? ')
    if a == 'yes':
        break # breaks out of the loop
