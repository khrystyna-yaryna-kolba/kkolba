from context import Context
from strategy import *
from observer import Observer
from logger import Logger
from event import Event
import sys
import copy
def menu():

    lis = LinkedList()
    context = Context()
    # Logger.file = "testtest.txt"
    Logger.clear_file()
    observer = Observer()
    observer.subscribe("add", Logger.print_to_file)
    observer.subscribe("remove", Logger.print_to_file)
    observer.subscribe("transform", Logger.print_to_file)

    while True:
        try:
            choice = input("enter your choice \n 1 - first strategy \n 2 - second strategy \n 3 - generate"
                           "\n 4 - remove \n 5 - remove in range \n 6 - method \n 7 - print list \n 8 - exit \n")
            if choice == "1":
                context.strategy = FirstStrategy()
            elif choice == "2":
                context.strategy = SecondStrategy()
            elif choice == "3":
                lis = use_strategy(lis, context, observer)
            elif choice == "4":
                pos = input_int("position to remove")
                lis_copy = copy.deepcopy(lis)
                lis.remove(pos)
                Event("remove", {"list before removal": lis_copy,"removal position": pos, "result list" : lis}).notify(
                    observer)
            elif choice == "5":
                a, b = input_int_range()
                lis_copy = copy.deepcopy(lis)
                lis.remove_in_range(a,b)
                Event("remove", {"list before removal in range": lis_copy, "removal range": (a, b), "result list": lis}).notify(
                    observer)
            elif choice == "6":
                k = input_int("input k to perform transform method with current list")
                lis_copy = copy.deepcopy(lis)
                lis = LinkedList.transform(lis, k)
                Event("transform", {"list before transforming": lis_copy, "k" : k,  "result list": lis}).notify(
                    observer)
            elif choice == "7":
                print(lis)

        except:
            e = sys.exc_info()[1]
            print("Error: ", str(e))
            continue

        if choice == "8":
            observer.unsubscribe("add")
            observer.unsubscribe("remove")
            observer.unsubscribe("transform")
            exit()
        else:
            continue

def use_strategy(lis, context, observer):
    if isinstance(context.strategy, FirstStrategy):
        n = input_non_negative_int("input number of elements to generate: ")
        a, b = input_int_range()
        pos = input_non_negative_int("input pos: ")
        lis_copy = copy.deepcopy(lis)
        lis = context.execute_strategy(lis, pos, n, a, b)
        Event("add", {"list before add": lis_copy, "pos to add": pos, "result list": lis}).notify(
            observer)
    elif isinstance(context.strategy, SecondStrategy):
        f = Validation.validate_file_name(input("input file name to read from: "), "json")
        pos = input_non_negative_int("input pos: ")
        lis_copy = copy.deepcopy(lis)
        lis = context.execute_strategy(lis, pos, f)
        Event("add", {"list before add": lis_copy, "pos to add": pos, "result list": lis}).notify(
            observer)
    else:
        raise ValueError("context strategy is not valid, try to initialize it")
    return lis

# main
menu()
