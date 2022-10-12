from container_collection import ContainerCollection
from container import Container
import sys

def menu():
    containers = ContainerCollection()

    while True:
        try:
            choice = input("enter your choice \n 1 - read from file \n 2 - search in the current collection of containers "
                       "\n 3 - add new Container to current collection \n 4 - print current collection \n 5 - sort "
                       "collection by property(number by default) \n 6 - delete Container from collection by ID \n 7 "
                       "- edit container by ID \n 8 - write collection to json file \n 9 - write collection to txt "
                           "file \n 10 - add new Container "
                           "to txt file \n 11 - add new Container to json file \n 12 - exit \n")
            if choice=="1":
                name = input("Input file name to read from(.json): \n")
                containers.read_json_file(name)
            elif choice == "2":
                s = input("Type what do you want to find: \n")
                f = containers.search(s)
                print("Results: \n")
                print(f)
            elif choice == "3":
                el = Container(**Container.input_container(*Container.default_props()))
                containers.add_element(el)
            elif choice=="4":
                print(containers)
            elif choice =="5":
                attr = input("property to sort by, -1 to perform default \n (valid: {}) \n".format(" ".join(Container.default_props())))
                if attr =="-1":
                    containers.sort()
                else:
                    containers.sort(attr)
            elif choice =="6":
                id = input("enter id that you want to delete: \n")
                containers.delete_by_id(id)
            elif choice =="7":
                id = input("enter id that you want to edit: \n")
                prop = input("input property you want to edit \n")
                val = input("input new value for chosen property \n")
                containers.edit_by_id(id, prop, val)
            elif choice =="8":
                f = input("enter file name:(.json) \n")
                containers.write_to_json_file(f)
            elif choice =="9":
                f = input("enter file name:(.txt) \n")
                containers.write_to_txt_file(f)
            elif choice =="10":
                el = Container(**Container.input_container(*Container.default_props()))
                f = input("enter file name to add Container to:(.txt) \n")
                el.add_to_text_file(f)
            elif choice =="11":
                el = Container(**Container.input_container(*Container.default_props()))
                f = input("enter file name to add Container to:(.json) \n")
                el.add_to_json_file(f)
        except:
            e = sys.exc_info()[1]
            print("Error: ", str(e))
            continue

        if choice == "12":
            exit()
        else:
            continue





menu()