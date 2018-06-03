#01-yield keyword


'''
At a glance, the yield statement is used to define generators,
 replacing the return of a function to provide a result to 
 its caller without destroying local variables. Unlike a 
 function, where on each call it starts with new set of 
 variables, a generator will resume the execution where 
 it was left off.Jan 24, 2013

'''

# https://www.pythoncentral.io/python-generators-and-yield-keyword/


def countdown(n):
 while n > 0:
 yield n
 n -= 1
>>> for i in countdown(5):
... print i,
...
5 4 3 2 1
>>>