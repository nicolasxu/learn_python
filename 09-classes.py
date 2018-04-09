# Python allows multiple base classes

# a derived class can override any methods of its base class or classes

# As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation



# Scope example

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
        # the global assignment changed the module-level binding

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

"""
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""

# Class Definition Syntax

class ClassName:
  pass
# class keyword will create a its own namespace (variable scope)


class MyClass:
  """ A simple example class"""
  i = 12345
  def __init__(self): # __init__ is constructor
    self.data = []
  def f(self):
    return 'hello world!'
#  __doc__ to access doc string

x = MyClass() # create new instance of class and assign it to x
xf = x.f() 
xf() # this works, why? instance object is passed as the first argument of the function


# example

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
# res: (3.0, -4.5)



# Example:

class Dog:

    kind = 'canine'         # class variable shared by all instances
    tricks = []             # !!!!!!!!!!!!! note: this is class variable, 
                            # not instance variable
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'

# Example of class variable
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']



# Example, correct way of doing instance variables

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']


# There is no private data member in Python class

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# Example: member method calling member method

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.


# 9.5. Inheritance
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

class DerivedClassName(modname.BaseClassName):
# Derived classes may override methods of their base classes
#  (For C++ programmers: all methods in Python are effectively virtual.)
# How to call base class method: 
BaseClassName.methodname(self, arguments)

isinstance()
isinstance(obj, int)
issubclass()
issubclass(bool, int) # True



# Mutiple Inheritance
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>


# 9.6. Private Variables (name mangling)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
# Note that the mangling rules are designed mostly to avoid accidents;
# it still is possible to access or modify a variable that is considered private. 


# Example

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000



# 9.8 Iterators
# Behind the scene, they all use  __iter__() and __next__()
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration


# Implement iterator class is implemnt
# __iter__() and __next__() method

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
>>>
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s



# 9.9 Generator
# Generators are a simple and powerful tool for creating iterators.
# In addition to automatic method creation and saving program state

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
>>>
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g


# 9.10. Generator Expressions

>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

>>> unique_words = set(word  for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
















