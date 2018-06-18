# 05-tornado.txt
'''
what is python tornado?
Tornado is a Python web framework and asynchronous networking lib.
- non-blocking network I/O, good for long polling, Websocket, long-lived connection to each user.

www.tornadoweb.org
'''
# Hellow world example

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
