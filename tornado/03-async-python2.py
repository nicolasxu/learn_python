from tornado.httpclient import AsyncHTTPClient
from tornado import gen

@gen.coroutine
def async_fetch_gen(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)


res = async_fetch_gen('http://google.com')
print(res)
# <tornado.concurrent.Future object at 0x7f4770336c10>

