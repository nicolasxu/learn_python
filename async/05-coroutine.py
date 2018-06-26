# 05-coroutine

'''
Coroutines
• If you use yield more generally, you get a coroutine
• These do more than just generate values
• Instead, functions can consume values sent to it.
'''

>>> g = grep("python")
>>> g.next() # Prime it (explained shortly)
# print: Looking for python
>>> g.send("Yeah, but no, but yeah, but no")
>>> g.send("A series of tubes")
>>> g.send("python generators rock!")
# print: python generators rock!
>>>
'''
• Sent values are returned by (yield)
'''