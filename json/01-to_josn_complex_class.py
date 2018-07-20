from attr import (
    attrs,
    attrib,
    Factory
)
from tornado.concurrent import Future
import logging
import json

def future_attrib(future_type, **kwargs):
    return attrib(init=False, repr=False, default=Factory(future_type))


@attrs
class ContainerDeliveryRequest(object):
    """
    A request for a flexbot to deliver a container to a pick/place locale.
    """
    transfer_request = attrib()
    container = attrib()

    flexbot_id_future = future_attrib(Future)
    retrieval_execution_future = future_attrib(Future)
    locale_future = future_attrib(Future)

    delivery_execution_future = future_attrib(Future)
    acknowledged_future = future_attrib(Future)

    def __attrs_post_init__(self):
        self._attach_done_callback()


    def to_json(self):
        temp_dict = {}
        for key, val in self.__dict__.iteritems():
            if (isinstance(val, Future)):
                temp_dict[key] = self._future_to_str(val)
            else:
                temp_dict[key] = val
        return json.dumps(temp_dict)

    def __repr__(self):
        return self.to_json()

    @staticmethod
    def _future_to_str (futureObj):
        if futureObj.done():
            return futureObj.result()
        else:
            return 'Not Done'

    def _attach_done_callback(self):
        for key, val in self.__dict__.iteritems():
            if isinstance(val, Future):
                val.add_done_callback(self.dummy_callback)

    def dummy_callback():
        pass


ss = ContainerDeliveryRequest(1,2)
