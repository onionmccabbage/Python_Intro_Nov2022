# here 'comprehension' means to comprehensively deal with every member of a collection
# we already knowabout range and generator...
# tuple comprehension
odd_t  = (num for num in range(0, 101) if num%2 == 1) # this is called tuple comprehension
# list comprehension
even_l = [num for num in range(0, 101) if num%2 == 0] # this is list comprehension
# dictionary comprehension
# for example, we can count the occurences of letters in a string
s = 'dictionary comprehension will iterate over every member of a dictionary'
char_dict = {letter:s.count(letter) for letter in s}
print(char_dict)