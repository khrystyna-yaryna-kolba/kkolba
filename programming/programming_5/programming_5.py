from container_collection import ContainerCollection
from container import Container
import sys
from memento import Caretaker, FileCaretaker
def menu():
    containers = ContainerCollection()
    caretaker = Caretaker(containers)
    caretaker.backup("initial state of collection")
    file_caretaker = None
    f_contain = None
    while True:
        try:
            choice = input("enter your choice \n 1 - read from json file \n 2 - search in the current collection of containers "
                       "\n 3 - add new Container to current collection \n 4 - print current collection \n 5 - sort "
                       "collection by property(number by default) \n 6 - delete Container from collection by ID \n 7 "
                       "- edit container by ID \n 8 - write collection to json file"
                           "\n 9 - undo collection change \n 10 - redo collection change \n 11 - show history of collection changes "
                           "\n 12 - exit \n")
            if choice=="1":
                name = input("Input file name to read from(.json): \n")
                containers.read_json_file(name)
                caretaker.backup("reading from file")
            elif choice == "2":
                s = input("Type what do you want to find: \n")
                f = containers.search(s)
                print("Results: \n")
                print(f)
                caretaker.backup("searching {}".format(s))
            elif choice == "3":
                el = Container(**Container.input_container(*Container.default_props()))
                containers.add_element(el)
                caretaker.backup("adding new element into collection")
            elif choice=="4":
                print(containers)
            elif choice =="5":
                attr = input("property to sort by \n (valid: {}) \n".format(" ".join(Container.default_props())))
                containers.sort(attr)
                caretaker.backup("sorting collection {}".format(attr))
            elif choice =="6":
                id = input("enter id that you want to delete: \n")
                containers.delete_by_id(id)
                caretaker.backup("deleted element from collection")
            elif choice =="7":
                id = input("enter id that you want to edit: \n")
                prop = input("input property you want to edit \n")
                val = input("input new value for chosen property \n")
                containers.edit_by_id(id, prop, val)
                caretaker.backup("edited element in collection")
            elif choice =="8":
                file = input("enter file name:(.json) \n")
                if file_caretaker is None:
                    f_contain = ContainerCollection()
                    f_contain.read_json_file(file)
                    file_caretaker = FileCaretaker(f_contain, file)
                    file_caretaker.backup("initial backup")
                caretaker.backup("write to file")
                containers.write_to_json_file(file)
                f_contain.read_json_file(file)
                file_caretaker.backup("write to file")
            elif choice =="9":
                undo(file_caretaker, caretaker)
            elif choice =="10":
                redo(file_caretaker, caretaker, containers)
            elif choice == "11":
                caretaker.show_history()
        except:
            e = sys.exc_info()[1]
            print("Error: ", str(e))
            continue

        if choice == "12":
            exit()
        else:
            continue

def undo(file_caretaker, caretaker):
    if caretaker.get_last_change() == "write to file":
        file_caretaker.undo()
    caretaker.undo()

def redo(file_caretaker, caretaker, containers):
    if caretaker.get_next_change() == "write to file":
        file_caretaker.redo()
    elif caretaker.get_next_change().split()[0] == "searching":
        print("Results: \n")
        print(containers.search("".join(caretaker.get_next_change().split()[1:])))
    caretaker.redo()
menu()