# here we explore simple unit testing
import doctest # doctest lets us write simple unit tests for our code

def cube(x):
    '''this function will take a number and return the cube of that number
    >>> cube(3)
    999
    '''
    return x*x*x

if __name__ == '__main__':
    print( cube(3) )  # 3 cubed is 27
    print( cube(-3) ) # -3 cubed is -27
    print( cube(1)  ) # 1 cubed is 1
    print( cube(30) ) # 30 cubed is 2700
    doctest.testmod()