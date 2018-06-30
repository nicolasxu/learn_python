# 02. __iter__.py

# https://github.com/bslatkin/effectivepython/blob/master/example_code/item_17.py
# make a class iterable
# Example 10

class ReadVisits(object):
'''
a container class that
implements the iterator protocol.
'''
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


# Example 11
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

'''
When Python sees a statement like
for x in foo it will actually call iter(foo). The iter built-in
function calls the foo.__iter__ special method in turn. The __iter__
method must return an iterator object (which itself implements the
63__next__ special method). Then the for loop repeatedly calls the next
built-in function on the iterator object until it’s exhausted (and raises a
StopIteration exception).

'''

'''
The protocol
states that when an iterator is passed to the iter built-in function, iter will
return the iterator itself. In contrast, when a container type is passed to iter,
a new iterator object will be returned each time
'''