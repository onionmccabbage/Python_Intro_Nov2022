# we need a 'Todo' class to encapsulate id, userId, title and completed
# userId and id will be positive integers or 999
# title will be a non-emtpy string or 'default'
# completed will be boolean True or False, default to False
# all these properties will be accessed via get/set methods

class Todo(object): # by default all classes inherit from 'Object'
    def __init__(self, id, userId, title, completed):
        self.id        = id
        self.userId    = userId
        self.title     = title
        self.completed = completed
    # we can write validator methods (setter methods)
    @property # this is the modern syntax for making get/set methods into properties
    def title(self):
        return self.__title
    @title.setter # decorator syntax
    def title(self, new_title): # this is the setter method for the title
        if type(new_title)== str and new_title != '':
            self.__title = new_title
        else:
            # self.__title = 'default'
            raise Exception # problem - the todo really needs a title string
    @property
    def id(self): # this is the getter method
        return self.__id
    @id.setter
    def id(self, new_id): # this is the setter method
        if type(new_id)==int and new_id>0:
            self.__id = new_id
        else:
            self.__id = 999
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, new_userId):
        if type(new_userId)==int and new_userId>0:
            self.__userId = new_userId
        else:
            self.__userId = 999
    @property
    def completed(self):
        return self.__completed
    @completed.setter
    def completed(self, new_completed):
        if type(new_completed)==bool:
            self.__completed = new_completed
        else:
            self.__completed = False
    # we can tell our class how to present itself when printed
    def __str__(self): # __str__ is ALWAYS use by the print statement
        return 'Title:{} \nid:{} \nuserId:{} \ncompleted:{}'.format(self.title, self.id, self.userId, self.completed)

if __name__ == '__main__':
    t1 = Todo(1, 4, 'Learn Python Classes', False)
    t2 = Todo(-2, True, 'ok', 3333) # some of these will be rejected
    try:
        t3 = Todo(99, 99,'This Works' ,False) # this should raise an exception
    except Exception as err:
        print(err)
    # if we print an instance of our class it will use the __str__ method
    print(t1.title)
    print(t3)

