from .node import Node
from threading import Thread as _Thread
from pygame.time import Clock as _Clock
from .window import Window as _Window
import os as _os
from .input import Input
from .vector2 import Vector2


class Engine(Node):
    """Engine Class"""
    _target_fps = 60
    _running = True

    # engine control
    @classmethod
    def set_target_fps(cls, fps):
        cls._target_fps = fps

    # engine control
    @classmethod
    def stop(cls, window):
        cls._running = False
        cls.emit_signal("engine_stopped")
        window.destroy()

    # signal callback
    def _on_window_closed(self):
        Engine.stop(self.window)  # auto-close window
        quit(0)  # exit program

    def __init__(self, title="Window", favicon=None, position=Vector2(1600, 100)):
        super().__init__()  # init Node
        # init and set name
        self.window = _Window.create(title)
        # move window
        self.window.geometry(f"+{position.x}+{position.y}")
        self.connect("window_closed", self, "_on_window_closed")
        self.window.protocol(  # setup exit signal
            "WM_DELETE_WINDOW",
            lambda: self.emit_signal("window_closed"))
        if favicon != None:
            self.window.iconbitmap(favicon)

        # _NET_WM_ACTION_RESIZE # resize signal

        try:  # call _ready
            if getattr(self, "_ready"):
                self._ready()
        except AttributeError:
            pass

        try:  # setup _process
            if getattr(self, "_process"):
                _Thread(target=self.__process,
                        args=[self],
                        name="EngineProcess").start()
        except AttributeError:
            pass

        # start Tkinter
        self.window.mainloop()  # blocking code

    @classmethod
    def __process(cls, self):
        _clock = _Clock()
        while cls._running:
            _clock.tick(cls._target_fps)
            self._process()
