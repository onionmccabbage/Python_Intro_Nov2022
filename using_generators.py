# Python includes a 'generator' object

def main():
    # range
    r = range(0, 22, 3) # start, stop-before, step
    # list
    num_l = [ num for num in range(0, 100, 5) ] # square brackets return an in-memory list
    print(num_l, type(num_l))

    # generator - the values do not persist in memory - they can be 'yielded'
    num_g = ( num for num in range(0, 100, 5) ) # ound brackets return a generator object
    print(num_g, type(num_g))
    # use the generator to yield values
    print( 'The generator yields its next value as {}'.format( num_g.__next__() ) ) # 0
    print( 'The generator yields its next value as {}'.format( num_g.__next__() ) ) # 5
    print( 'The generator yields its next value as {}'.format( num_g.__next__() ) ) # 10

    # we can iterate over all the remaining values in our generator
    for item in num_g:
        print( item, end=', ' ) # 15, 20, ...95

    if isinstance(num_l, list): # isinstance can check list, tuple, string, boolean, float, int, None
        print('yep it is a list')

if __name__ == '__main__':
    main()