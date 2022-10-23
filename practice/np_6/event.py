class Event:
    def __init__(self, name, args):
        self._name = name
        self._args = args

    def __str__(self):
        return "Event " + self._name + ":  " +  " , ".join(str(k)+": "+str(self._args[k]) for k in self._args.keys())

    def notify(self, observer):
        if self._name in observer._events:
            observer._events[self._name](self)
            #print("{} notified".format(self._name))
