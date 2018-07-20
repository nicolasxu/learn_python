# http://www.tornadoweb.org/en/stable/guide/async.html

from tornado.concurrent import Future

def async_fetch_manual(url):

    http_client = AsyncHTTPClient()

    my_future = Future()

    fetch_future = http_client.fetch(url)

    def on_fetch(f):
        my_future.set_result(f.result().body)

    fetch_future.add_done_callback(on_fetch)

    return my_future

