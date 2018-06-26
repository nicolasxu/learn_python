# 22. "with" statement

# http://preshing.com/20110920/the-python-with-statement-by-example/

with open('output.txt', 'w') as f:
    f.write('Hi there!')
'''
file is guarantee to close, not matter what
'''


# making a class work with "width" statement
'''
There are two ways to support the with statement:
by implementing a context manager class, or
by writing a generator function.
'''

'''
Here’s the first approach. To implement a context manager,
we define a class containing an __enter__ and __exit__ method.
'''
# pycairo drawing
cr.translate(68, 68)
for i in xrange(6):
    cr.save()
    cr.rotate(2 * math.pi * i / 6)
    cr.rectangle(-25, -60, 50, 40)
    cr.stroke()
    cr.restore()

class Saved():
    def __init__(self, cr):
        self.cr = cr
    def __enter__(self):
        self.cr.save()
        return self.cr
    def __exit__(self, type, value, traceback):
        self.cr.restore()

#usage:
cr.translate(68, 68)
for i in xrange(6):
    with Saved(cr):
        cr.rotate(2 * math.pi * i / 6)
        cr.rectangle(-25, -60, 50, 40)
        cr.stroke()



# Implementing the Context Manager as a Generator
from contextlib import contextmanager

@contextmanager
def saved(cr):
    cr.save()
    yield cr
    cr.restore()

# 2nd version
@contextmanager
def saved(cr):
    cr.save()
    try:
        yield cr
    finally:
        cr.restore()
