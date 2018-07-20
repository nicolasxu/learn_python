from tornado.concurrent import (Future, return_future)
from tornado import gen


@return_future
def future_func(callback):
	return 10

@gen.coroutine
def callback1():
	return 20

def dcb(f):
	print (f.result())
	pass

ss = callback1()
ss.add_done_callback(dcb)
print (ss)

