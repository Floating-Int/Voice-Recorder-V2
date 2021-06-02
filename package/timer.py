from .node import Node

from threading import Thread as _Thread
from time import sleep as _sleep


class Timer(Node):
    def __init__(self):
        self.wait_time = 1.0  # seconds
        self.one_shot = False
        self.autostart = False
        self.paused = False
        self._is_active = False

        self._thread = None

    def start(self):
        self._is_active = True
        self._thread = _Thread(target=self._process_time)
        self._thread.start()
        self._emit_signal_started()

    def _process_time(self):
        _sleep(self.wait_time)
        self._emit_signal_timeout()
        if self.autostart and self._is_active:  # if going to use recursive loop
            self._process_time()  # recursive loop
        self._is_active = False   # when finished recursive loop
        self._emit_signal_stopped()

    def stop(self):
        self._is_active = False
        self._emit_signal_stopped()

    def _emit_signal_timeout(self):
        """
        built-in signal 'timeout'
        """
        self.emit_signal("timeout")

    def _emit_signal_started(self):
        """
        built-in signal 'started'
        """
        self.emit_signal("started")

    def _emit_signal_stopped(self):
        """
        built-in signal 'stopped'
        """
        self.emit_signal("stopped")

    def is_active(self):  # getter
        return self._is_active
