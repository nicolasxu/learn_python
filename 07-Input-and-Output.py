a = 10
b = 3,4,5
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(repr(s))



for x in range(1, 11):
  print( repr(x).rjust(2), repr(x*x).rjust(3), end=" ")



for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


'12'.zfill(5)
'-3.14'.zfill(7)
'3.14159265359'.zfill(5)

print('We are the {0} who say "{1}!"'.format('knights', 'Ni'))

print('{1} and {0}'.format('spam', 'eggs'))



print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
  print('{0:10} ==> {1:10d}'.format(name, phone))



# open file

f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()
f.closed



f.read()
'This is the entire file.\n'
f.read()
''


f.readline()
'This is the first line of the file.\n'

>>> f.readline()
''


>>> for line in f:
...     print(line, end='')
...
"""
This is the first line of the file.
Second line of the file
"""

>>> f.write('This is a test\n')
15

>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18

f.tell() # return pointer position 
f.seek(offset, from_what)


## 7.2.2. Saving structured data with json

>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'


json.dump(x, f) # dump to a file, f is file 

x = json.load(f) # load json from file




