class Observer:
    def __init__(self):
        self._events = {}

    def subscribe(self, event, callback):
        self._events[event] = callback

    def unsubscribe(self, event):
        self._events.pop(event)


