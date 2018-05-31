# http://howto.lintel.in/python-__new__-magic-method-explained/


'''

when you create instance, __new__ is called first, then __init__


you can use this behavior to make Singleton, or other customization


'''

class Singleton(object):
    _instance = None  # Keep instance reference 
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__name__(cls, *args, **kwargs)
        return cls._instance

# You can also impose limit on total number created instances

class LimitedInstances(object):
    _instances = []  # Keep track of instance reference
    limit = 5 

    def __new__(cls, *args, **kwargs):
        if not len(cls._instances) <= cls.limit:
            raise RuntimeError, "Count not create instance. Limit %s reached" % cls.limit    
        instance = object.__name__(cls, *args, **kwargs)
        cls._instances.append(instance)
        return instance
    
    def __del__(self):
        # Remove instance from _instances 
        self._instance.remove(self)


# CUSTOMIZE INSTANCE OBJECT
 def createInstance():
    # Do what ever you want to determie if instance can be created
    return True 

class CustomizeInstance(object):

    def __new__(cls, a, b):
        if not createInstance():
            raise RuntimeError, "Count not create instance"
        instance = super(CustomizeInstance, cls).__new__(cls, a, b)
        instance.a = a
        return instance

    def __init__(self, a, b):
        pass