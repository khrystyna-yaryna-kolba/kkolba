from abc import ABC, abstractmethod
import copy
class Memento(ABC):
    #for caretaker
    @abstractmethod
    def get_state_name(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, lst, ids, name):
        self._lst = copy.deepcopy(lst)
        self._ids = copy.deepcopy(ids)
        self._name = name
    def get_state_name(self):
        return self._name
    def __str__(self):
        return str(self._name)
    #for originator
    def get_state(self):
        return copy.deepcopy(self._lst), copy.deepcopy(self._ids.copy())


class Caretaker:
    STEPS_SIZE = 6  # number of max possible steps

    def __init__(self, container_collection):
        self._mementos = []
        self._originator = container_collection
        self._cur_state = -1
    def get_last_change(self):
        return self._mementos[self._cur_state].get_state_name()
    def get_next_change(self):
        if self._cur_state + 1 > (len(self._mementos) - 1):
            return "nothing"
        else:
            return self._mementos[self._cur_state+1].get_state_name()
    def backup(self, name):
        print("backup...")
        if self._cur_state != (len(self._mementos) - 1):
            self._mementos = self._mementos[:self._cur_state+1]
        if len(self._mementos) == Caretaker.STEPS_SIZE:
            self._mementos = self._mementos[1:]
            self._cur_state -= 1
        self._cur_state += 1
        self._mementos.append(self._originator.save(name))

    def undo(self):
        if self._cur_state <=0:
            print("nothing to undo")
            return
        print("undoing {}".format(self._mementos[self._cur_state].get_state_name()))
        self._cur_state -= 1
        self._originator.restore(self._mementos[self._cur_state])

    def redo(self):
        if self._cur_state >= (len(self._mementos) - 1):
            print("nothing to redo")
            return
        self._cur_state += 1
        print("redoing {}".format(self._mementos[self._cur_state].get_state_name()))
        self._originator.restore(self._mementos[self._cur_state])

    def show_history(self):
        print("History: ")
        for i, m in enumerate(self._mementos):
            if i == self._cur_state:
                print("-- current state: ")
            print("   ***   ", m.get_state_name())


class FileCaretaker(Caretaker):
    STEPS_SIZE = 6  # number of max possible steps
    def __init__(self, container_collection, filename):
        Caretaker.__init__(self, container_collection)
        self._filename = filename
    def backup(self, name):
        if self._cur_state != (len(self._mementos) - 1):
            self._mementos = self._mementos[:self._cur_state+1]
        if len(self._mementos) == Caretaker.STEPS_SIZE:
            self._mementos = self._mementos[1:]
            self._cur_state -= 1
        self._cur_state += 1
        self._mementos.append(self._originator.save(name))
    def undo(self):
        if self._cur_state <=0:
            return
        self._cur_state -= 1
        self._originator.restore(self._mementos[self._cur_state])
        self._originator.write_to_json_file(self._filename)

    def redo(self):
        if self._cur_state >= (len(self._mementos) - 1):
            return
        self._cur_state += 1
        self._originator.restore(self._mementos[self._cur_state])
        self._originator.write_to_json_file(self._filename)
