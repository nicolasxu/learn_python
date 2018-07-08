
str = 'Coroutine is implemented as an extension to generators '
'''


Python can work around all these issues with coroutines. 

Coroutines let you have many seemingly simultaneous 
functions in your Python programs. They’re implemented as 
an extension to generators 


The cost of starting a generator coroutine is a function call. 
Once active, they each use less than 1 KB of memory until they’re exhausted.

'''


'''

Coroutines work by enabling the code consuming a generator to 
send a value back into the generator function after each 
yield expression. The generator function receives the value 
passed to the send function as the result of the corresponding 
yield expression.


'''