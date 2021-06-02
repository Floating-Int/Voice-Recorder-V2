# main Node Class
from .signal import Signal


class Node(object):
    _nodes = []

    def __init__(self, **kwargs):  # needed for refference
        Node._nodes.append(self)

        #print("New Node Kwargs:")
        for key, value in kwargs.items():
            setattr(self, key, value)
            #print(key, ":", value)

    def __repr__(self):
        return str(self.__class__.__name__)

    @classmethod
    def new(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @staticmethod
    def connect(signal, target, method):
        Signal._signals.append(  # append new instance if Signal
            Signal(signal, target, method)
        )  # to Array in Signal class

    @staticmethod
    def emit_signal(signal):
        Signal._call_signal(signal)
