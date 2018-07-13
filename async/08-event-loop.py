#08-event-loop.py

# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

'''

Essentially all an event loop does is wait for events to
happen before matching each event to a function that we
have explicitly matched with said type of event.

'''

'''
A good example of this would be a simple web server,
say we have an endpoint on our server that serves our
website which features a multitude of different pages.
Our event loop essentially listens for requests to be
made and then matches each of these requests to its
associated webpage.

'''