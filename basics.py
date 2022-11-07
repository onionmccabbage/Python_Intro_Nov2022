# here is a Python comment
a = 3   # integer
b = 7.2 # float

# primitive data types: integer, float, boolean, None
print(a+b)
print(a/b)
print(b//a) # show the integer division
print(b%a)  # show remainder
print(b**3) # raise to the power
# data-types are not fixed  - we can dynamically change the data type
a = 'hello' # string
b = True # or False

# collections of data members
c = 'this is a collection of characters' # a string is a collection data-type
# all indexed collections begin at zero
print( c[5] ) # i
# we can use square-brackets to pick a selection of members
print( c[2:13:2] ) # [start : stop-before : step]
print( c[::] ) # defaults to [0::1]
print( c[::-1] )
# strings are immutable
# c[0] = 'T' # oops
c = "altered" # single or double quotes are fine
print(c)
# list: a mutable indexed collection of any other data type
my_list = [3, 2, 1] # square brackets indicate a list
my_list[1] = 'altered'
my_list.append(b)
print(my_list)
# we can check data types
print( type(my_list), type(my_list[0]), type(my_list[1]), type(my_list[3]) )
# tuple: immutable indexed collection of any types
my_tuple = (8, 7, 6.3, False, a) # round brackets indicate a tuple
# my_tuple[3] = 'oops'
print(my_tuple[::-1], type(my_tuple))
# we can receive input from the user (in python 2 use raw_input)
q = input('please enter a number ') # we ALWAYS get a string
# we can cast the input to a number
q_float = float(q)
print(q_float, type(q_float))
# be careful
i = input('we need an integer ')
i = int(float(i)) # this is robust - make a float then make an int
print(i, type(i))