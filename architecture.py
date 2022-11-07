# Python has many built-in libraries
# we can import functionality like this
import random # here we import the entire 'random' library
# alternative is to import just the bits we need
from random import randint # here we only import random.randint
r = randint(-10, 10) # we can access parts of the 'random' library like this
print(r)

for i in range(1,100):
    r = randint(0,100)
    print(r, end=', ') # by default 'print' will terminate with a new line