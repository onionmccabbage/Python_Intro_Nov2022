# we can import code from other modules
# this is an example of 'namespacing'
import my_modules.h_table # we import the entire module
# CAUTION - ALL immediate code gets run when we import
import my_modules.w_table as web

furniture = my_modules.h_table.table(3,4)
print(furniture)
web_table = web.table(5,6)
print(web_table)

# Python uses the 'def' keyword to define a function
def makeSquare(x): # all functions need a colon - they have a code block
    return x*x # i.e. the square of x

def hypot(x=3, y=4): # these are positional arguments (here they are given defaults)
    ''' here is a docstring - documentation for this function
    triple-quotes allow new lines within the atring
    Function to calculate the hypotenuse of a right-angle triangle
    arguments x and y return h
    '''
    h = (x*x + y*y)**0.5 # raise to power of 0.5 means square root
    return h

if __name__ == '__main__':
    # call our functions
    print(makeSquare(2))
    print(makeSquare(-2))
    print(makeSquare(20))
    print(makeSquare(42))
    result = hypot(30, 40)
    # result = hypot() # this will use the default values
    print(result) # 50
