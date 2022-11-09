#our classes can inherit from other classes
from a import Person

# here we inherit everything from Person
class Coder(Person):
    ''' in addition to name, age, email
    a Coder also has 'language' '''
    def __init__(self, n, a, e, l):
        super().__init__(n, a, e) # call the init method of the parent class
        self.language = l
    # make language act like a property
    def setLang(self, lang):
        if type(lang)==str and lang !='':
            self.__lang = lang
        else:
            self.__lang = 'Python'
    def getLang(self):
        return self.__lang
    language = property(getLang, setLang)
        
if __name__ == '__main__':
    # create instances of our Coder
    c = Coder('Timnit', 38, 'timnit@nasa.ie', 'Python')
    c.language = 'Jython'
    print(c.email, c.language)