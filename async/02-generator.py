02-generator
'''
Generators

- Behavior is quite different than normal func
- Calling a generator function creates an
generator object. However, it does not start
running the function.
- The function only executes on next()
'''

def countdown(n):
 print "Counting down from", n
 while n > 0:
 yield n
 n -= 1


>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>>

################################
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.next()
Counting down from 10
10
>>>

# yield produces a value, but suspends the function
# • Function resumes on next call to next()
>>> x.next()
9
>>> x.next()
8
>>>