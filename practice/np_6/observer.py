class Observer:

    def __init__(self):
        self._events = {}

    def subscribe(self, event, callback):
        self._events[event] = callback

    def unsubscribe(self, event):
        self._events.pop(event)


class Event:
    def __init__(self, name, args):
        self._name = name
        self._args = args

    def __str__(self):
        return "Event " + self._name + ":  " +  " , ".join(str(k)+": "+str(self._args[k]) for k in self._args.keys())

    def notify(self, observer):
        if self._name in observer._events:
            observer._events[self._name](str(self))
            #print("{} notified".format(self._name))


class Logger:
    file = "log.txt"
    @staticmethod
    def print_to_file(data):
        f = open(Logger.file, mode='a', encoding='utf-8')
        f.write(data + "\n")
        f.write("\n")
        f.close()

    @staticmethod
    def clear_file():
        f = open(Logger.file, mode='w', encoding='utf-8')
        f.close()
