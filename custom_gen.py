# generators are useful snce they yield values wthout requiring loads of memory to store the values

# here we will generate a series of square nubmers
def genSquareNum(n=0, stop=10, step=1):
    '''
    Generate the squares of numbers from n to 'stop' every 'step'
    '''
    number =n 
    stop_at = stop
    while number < stop_at:
        number += step
        yield number**2 # yield instead of return - yield makes this a generator

if __name__ == '__main__':
    g = genSquareNum() # we now have an instance of our generator (we could inject values for start etc.)
    print(g.__next__()) # 1
    print(g.__next__()) # 4
    print(g.__next__()) # 9
    print(g.__next__()) # 16
    # we can iterate over our generator
    for x in g:
        print(x, end=", ")
    # our generator instance is now exhausted
    # print(g.__next__())