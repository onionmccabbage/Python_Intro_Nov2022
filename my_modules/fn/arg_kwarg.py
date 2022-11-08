# functions can take arguments either as positional arguments or as keyword arguments
def pow(x, y): # these are positional aruments. The value of x will come before the value of y
    '''raise x to the power of y'''
    return x**y

# all positional arguments will exist in a tuple in the function
def positionalArgs( *args ): # the asterisk tells python to gather all the positional arguments into a tuple
    print(type(args), args) # we get a tuple containing all the positional arguments
    # we can act differently depending on the number of arguments passed in
    if len(args) == 0: # no arguments were passed in 
        print('no arguments were passed in')
    elif len(args) == 1:
        print('called with one argument {}'.format(args[0]))
    else:
        print('more than one argument was received')
        for item in args:
            print(item)

# all keyword arguments can be gathered together into a dictionary
def keywordArgs( **kwargs ): # the ** tells python to gather any keyword args into a dictionary
    print(type(kwargs)) # dict
    # we can iterate over members of a dictionary
    for (k,v) in kwargs.items():
        print('key: {} has value:{}'.format(k,v))

if __name__ == '__main__': # NB 'args' and 'kwargs' is merely a convention 
    # pass in positional arguments x then y
    r = pow(3, 2) # 9 (3**2 is 9)
    # we can specify which argument goes where
    r = pow(y=4, x=2) # these are keyword arguments

    print(r)
    # use our positionalArgs function
    positionalArgs() # no arguments
    positionalArgs('single') # a single argument
    positionalArgs(8,7,6,5,True,'wow',None, (7,), []) # we can pass as many or as few args as we like
    # use our kwargs function - we pass args as keyword args
    keywordArgs(x=1, b=True, d={}, l=[1,2,3], t='text')