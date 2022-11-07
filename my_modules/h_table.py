# here we encapsulate some featuess of a furniture table
def table(width, height):
    t = {'width':width, 'height':height} # make a dictionary
    return t

# this is a very common check we use in Python modules
if __name__ == '__main__':
    # exercise this code
    t = table(1,2)
    print(t)

    # every module is given a name by Python
    # the module which is being executed is ALWAYS given the name __main__ by Python
    print('The h_table module has been given a name of:', __name__) # the name is always stroed in  __name__