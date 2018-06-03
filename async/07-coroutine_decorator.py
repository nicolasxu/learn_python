07-coroutine_decorator

• Remembering to call .next() is easy to forget
• Solved by wrapping coroutines with a decorator


def coroutine(func):
 	def start(*args,**kwargs):
 	cr = func(*args,**kwargs)
 	cr.next()
 	return cr
return start

@coroutine
def grep(pattern):
 ...
 
• I will use this in most of the future examples