# 01-Subject
import rx

from rx import Observable, Observer
from rx.subjects import Subject

stream = Subject()
stream.on_next(41)

class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

d = stream.subscribe(MyObserver())

stream.on_next(42)

d.dispose()
stream.on_next(43)