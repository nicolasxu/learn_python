# 01. itertools.islice.py

# https://docs.python.org/2/library/itertools.html#itertools.islice

'''
Make an iterator that returns selected elements from the iterable.
If start is non-zero
'''


# Example 6
address_lines = """Four score and seven years
ago our fathers brought forth on this
continent a new nation, conceived in liberty,
and dedicated to the proposition that all men
are created equal."""

with open('address.txt', 'w') as f:
    f.write(address_lines)

from itertools import islice
with open('address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))

