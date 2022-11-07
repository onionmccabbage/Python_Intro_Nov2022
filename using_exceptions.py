# Python has try...except in order for us to handle exceptions

def main(divisor):
    try:
        e = 99/divisor
        return e
    except ZeroDivisionError as err: # catch specific exceptions we might expect
        # we always have the option to format our print output
        print( 'There was a problem: {} when trying to divide by {}'.format(err, divisor) )
    except Exception as err: #we can allso catch more generic exceptions
        print('some other problem occured')
    finally:
        # this block always runs even if there was an exception
        print('all good')

if __name__ == '__main__':
    main(0)