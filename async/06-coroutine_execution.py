06-coroutine_execution

'''
Coroutine Execution
• Execution is the same as for a generator
• When you call a coroutine, nothing happens
• They only run in response to next() and send()
methods
'''
>>> g = grep("python") # no output was produced
>>> g.next() # On first operation, coroutine starts running
Looking for python
>>>

'''
Coroutine Priming
• All coroutines must be "primed" by first
calling .next() (or send(None))
'''
'''
This advances execution to the location of the
first yield expression.
'''