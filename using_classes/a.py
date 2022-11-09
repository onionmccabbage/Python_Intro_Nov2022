# use the built-in structures whenever possible
p = {'name':'Ada', 'age':42} # here we encapsulate a 'person'
p['age'] = True # oh dear - not what we need

# when the built-in structures do not provide what you need, then you make your own structure - a class
# e.g. enforce that the 'age' is a positive integer, and 'name' is a non-empty string
# we can declare a class like this:

# the brackets here are optional
class Person(): # by convention we use initial caps for classes
    '''This class encapsulates a 'Person' 
    Parameters: name, age, email
    'age' must be a positive interger
    'name' must be a non-empty string
    'email' is optional (can be an empty string)
    '''
    # we can write an __init__ method - called every time we use the class
    # we MUST provide 'self' for EVERY method of this class. 'self' refers to the class itself
    def __init__(self, n, a, e): # this is similar to a constructor
        # we COULD just call the name set method
        self.name = n # self.setName(n) # self.name is a property of this class
        self.age  = a # self.setAge(a) # we can use our methods to validate the initial values
        self.email  = e
    # we can write functions that belong to this class - they are called 'methods'
    def setName(self, new_name):
        '''name must be a non-empty string, or 'default' '''
        if type(new_name) == str and new_name != '':
            # Python does not have 'private' so we use __name
            self.__name = new_name # this is called name-mangling
        else:
            self.__name = 'default'
    def getName(self):
        return self.__name
    def setAge(self, new_age):
        '''validate that the age is a positive integer'''
        if int(float(new_age)) > 0:
            self.__age = new_age
        else:
            self.__age = 42 # provide a sensible default
    def getAge(self):
        return self.__age
    name = property(getName, setName) # make our methods look like properties
    age  = property(getAge, setAge)

if __name__ == '__main__':
    p1 = Person('Ada', 42, '') # here we create an instance of our class
    # p1.setName('Ada')
    # p1.name = True # calls the setter method for name
    p1.age = 0 # calls the setter method for age
    # p1.setAge(-99)
    print(p1.name, p1.age, p1.email, p1)