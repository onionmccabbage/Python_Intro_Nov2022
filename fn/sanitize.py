# we often need to sanitize data -
# clean it and check it is of the correct data type

# in this example we check to see if data is integer, float or boolean
# NB if the data is not a simple type, we need to return a value
def checkSimpleType(value):
    '''Take a value and check it is integer, float or boolean
    If it is, return the integer part of the value
    if it is any other data type, return 0
    '''
    simple = {int, float, bool} # here we have a set
    comp   = {list, tuple, dict, set}
    if type(value) in comp:
        return 0 # we choose to return 0 if its not a simple typ
    if type(value) in simple or value.isnumeric():
        return int(float(value))
    else:
        return 0

if __name__ == '__main__':
    print( checkSimpleType(1) )    # an integer
    print( checkSimpleType(1.23) ) # a foat
    print( checkSimpleType(True) ) # a boolean
    print( checkSimpleType([5,4,3]) ) # a list - expect 0
    print( checkSimpleType('42') ) # a numeric string
