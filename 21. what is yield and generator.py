# 21. what is yield and generator.py
# https://www.pythoncentral.io/python-generators-and-yield-keyword/
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()


>>> the_generator = search('Python', 'directory.txt')
>>> type(search)
<class 'function'>
>>> type(the_generator)
<class 'generator'>


>>> print(next(the_generator))
generator started
Anton Pythonio 111-222-333


>>> print(next(the_generator))
generator started
Fritz Pythonmann 128-256-512

>>> print(next(the_generator))
generator started
Guido Pythonista 123-456-789


############################# another example ###########################


def hold_client(name):
    yield 'Hello, %s! You will be connected soon' % name
    yield 'Dear %s, could you please wait a bit.' % name
    yield 'Sorry %s, we will play a nice music for you!' % name
    yield '%s, your call is extremely important to us!' % name


###################### example #############################
def buffered_read():
    while True:
        buffer = fetch_big_chunk()
        for small_chunk in buffer:
            yield small_chunk
