# https://www.programiz.com/python-programming/methods/built-in/getattr

'''



getattr() Parameters

The getattr() method takes multiple parameters:

    object - object whose named attribute's value is to be returned
    name - string that contains the attribute's name
    default (Optional) - value that is returned when the named attribute is not found


'''

'''
Return value from getattr()

The getattr() method returns:

    value of the named attribute of the given object
    default, if no named attribute is found
    AttributeError exception, if named attribute is not found and default is not defined


'''

The syntax of getattr() method is:

getattr(object, name[, default])

The above syntax is equivalent to:

object.name



class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)