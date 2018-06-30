# 25. __call__.py


# https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call-in-python


class Foo:
    def __init__(self, a, b, c):
        # ...

x = Foo(1, 2, 3) # __init__

###################################

class Foo:
    def __call__(self, a, b, c):
        # ...

x = Foo()
x(1, 2, 3) # __call__

'''
	So, the __init__ method is used when the class is called to initialize
	the instance, while the __call__ method is called
	when the instance is called
'''