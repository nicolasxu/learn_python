20-what is __dict__


'''
__dict__ is a specific dictionary that exists for each Python object, 
and contains the attributes of that object and their values. The
 double underscore is simply a Python convention for marking a 
 variable as "special," but you're free to modify it like any 
 other variable if you want.

'''

# https://linuxfollies.blogspot.com/2010/08/pythons-dict.html

Python class instance members are really dictionaries/mappings. For example,
    class Foo:
        def __init__(self, name=''):
            self.name = name
You can access the name member:
    In [2]: f = Foo('vito')

    In [3]: f.name
    Out[3]: 'vito'
You can also do:
    In [4]: f.__dict__['name']
    Out[4]: 'vito'
In fact, you can see all the data members:
    In [5]: f.__dict__
    Out[5]: {'name': 'vito'}