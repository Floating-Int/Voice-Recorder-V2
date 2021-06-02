from .node import Node
from tkinter import Tk

SCREEN_SIZE = (960, 540)


class Window:
    window = None

    @classmethod
    def set_title(cls, new_title):
        cls.window.title(new_title)

    # manual init - returns a window object
    @staticmethod
    def create(title="Window"):
        # HEIGHT, WIDTH = (300, 512) # standard
        HEIGHT, WIDTH = (300, 512)
        window = Tk()  # store in class
        window.minsize(HEIGHT, WIDTH)  # window min size
        window.maxsize(HEIGHT, WIDTH)  # window max size
        # window.geometry("x".join(
        #    map(lambda x: str(x), [HEIGHT, WIDTH])
        # ))
        window.title(title)
        return window
