#09-what-is-future.py

"Future is Placeholder for an asynchronous result."

# https://kite.com/python/docs/tornado.concurrent.Future

# https://docs.python.org/3.4/library/concurrent.futures.html#concurrent.futures.Future
# You can only use offical doc after you understand this concept.

'''

A Future encapsulates the result of an asynchronous operation.
In synchronous applications Futures are used to wait for the
result from a thread or process pool; in Tornado they are
normally used with IOLoop.add_future or by yielding them
in a gen.coroutine.

'''


from tornado.concurrent import Future
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
def async_fetch_future():
    http_client = AsyncHTTPClient()
    future = Future()
    fetch_future = http_client.fetch(
        "http://mock.kite.com/text")
    fetch_future.add_done_callback(
        lambda f: future.set_result(f.result()))
    return future

response = IOLoop.current().run_sync(
    async_fetch_future)
print response.body
'''
OUTPUT
We want to establish the idea that a computer language is not just
a way of getting a computer to perform operations but rather that it
is a novel formal medium for expressing ideas about methodology.
'''