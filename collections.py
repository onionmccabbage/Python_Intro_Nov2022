# here we explore the collection data-types in Python
l = list() # an empty list
l = [3, True, 'ciao', None, [8, 7, 6]] # any and all data types can populate a list
# we can access members
print( l[4][2] ) # 6

# Python has a 'range' object
r = range(100, 0, -3) # start at..., stop-before..., step...
for i in r: # the colon begins a block of cod
    print( i ) # notice the indentation (required)

# the block of code ends when we no longer indent
# we can create collections easily using range
odds = range(1, 100, 2)
for i in odds: # this is handy, since the values do not need to persistt in memory
    print(i)

# we may need to persist the range values in memory
odds = tuple( range(1, 100, 2) ) # or list if we may need to mutate members later
print(odds, type(odds))

# there are non-indexed collections: dictionary (mutable) (like a hash-map)
d1 = {'id':'Timnit', "age":42, 'member':True} # the curly brackets indicate this is a dictionary
# dictionary is a collection of key:value pairs. There is NO natural order to these
# access members like this
d1['id'] = 'Gebru'
print(d1['id'])
# we can access keys and values like this
print(d1.keys(), d1.values() )
# we can add new members
d1['famous'] = True
# to iterate over a dictionary
for (k, v) in d1.items(): # conventional way to iterate over the dictioanry items
    print(k, v)

# other creational techniques
w = dict() # an empty dictionary
# careful -
z = (7,) # this is a one-member tuple

# there is also the 'set' data-type: a collection of non-indexed unique values
s = {7, 6, 4, 7, 5, 2, 1, 3} # here the curly brackets are NOT a dictionary, they indicate a set
s.add(0) # sets are mutable
print(s, type(s)) # only unique members survive