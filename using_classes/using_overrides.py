# we can override many of the built-in features of Python
# we already saw the __str__ method, which overides how 'print' works

# for example we can write a class and specify that the equality operator should ignore case
class Word():
    '''
    This class overrides the equaliy operator to ignore case
    '''
    def __init__(self, text):
        self.text = text # here we choose not to use get/set property methods
    def __eq__(self, other_word): # here we override '=='
        return self.text.lower() == other_word.text.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    w1 = Word('hello')
    w2 = Word('Hello')
    w3 = Word('hELlo')
    print(w1 == w2) # True
    print(w1 == w3) # True