

class Signal:
    # [signal, target, method]
    _signals = []

    def __init__(self, signal, target, method):
        self._signal = signal  # name
        self._target = target   # target
        self._method = method  # method

    def __repr__(self):
        return self._signal

    @classmethod
    def _call_signal(cls, signal):
        for s in Signal._signals:
            if s._signal == signal:  # if name == signal_arg
                if not hasattr(s._target, s._method):
                    raise AttributeError(
                        f"In signal: '{s._signal}' - Target '{s._target}' ha no method '{s._method}'")
                getattr(s._target, s._method)()  # call function
