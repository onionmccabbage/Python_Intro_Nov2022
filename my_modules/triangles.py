# here we ask for TWO integers then calculate the hypotenuse
import fn.sanitize as san

def hypot(x,y):
    return (x*x + y*y)**0.5 # hypotenuse of a r.a. triangle

def main():
    # ask the user for two integers (input ALWAYS gives a string)
    x = input('Please enter a value for x ')
    y = input('Please enter a value for y ')
    # use our 'san' utility to check they are integers
    x_int = san.checkSimpleType(x)
    y_int = san.checkSimpleType(y)
    # call our 'hypot' function
    print( hypot(x_int, y_int) )

if __name__ == '__main__':
    main()