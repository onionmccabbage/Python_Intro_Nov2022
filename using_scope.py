# we aim not to polute the global namespace, but if we need to use it...
g = 'this is in the global scope'

def fn():
    global g # we now have access to 'g' from the global scope
    g = 'this is in the local scope'
    print(g) 

if __name__ == '__main__':
    fn()
    print(g)