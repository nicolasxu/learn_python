from tornado.concurrent import Future
from concurrent.futures import ProcessPoolExecutor
import time

def work(x):
	time.sleep(4)
	return 'work is finished'

def work_done(res):
	print ('work done callback triggered ' + res )
with ProcessPoolExecutor() as pool:
	my_future = Future()
	my_future = pool.submit(work, 'a')
	my_future.add_done_callback(work_done)
	print (my_future)
	print(my_future.result())

