# class methods and static methods

class Duck(object):
    count = 0 # this property belongs to the class, not to any instance of the class
    def __init__(self, n):
        self.name = n # we could validate using property get/set methods
        Duck.count += 1
    def __str__(self): # give our class a nice way to print itself
        return '{}'.format(self.name)
    @classmethod
    def numDucks(cls): # class methods take cls NOT self
        return cls.count
    @staticmethod
    def promo(): # no self, no cls - this is a static method
        return 'These ducks are brought to you by Angelas Duck Hospital'

if __name__ == '__main__':
    # we can call static methods on the class:
    print( Duck.promo() )
    donald = Duck('Donald')
    howard = Duck('Howard')
    ella   = Duck('Ella')
    print(Duck.numDucks()) # or Ducks.count