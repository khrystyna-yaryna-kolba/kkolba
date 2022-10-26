from context import Context
from strategy import *
import sys
def menu():

    lis = LinkedList()
    context = Context()

    while True:
        try:
            choice = input("enter your choice \n 1 - first strategy \n 2 - second strategy \n 3 - generate"
                           "\n 4 - remove \n 5 - remove in range \n 6 - method \n 7 - print list \n 8 - exit \n")
            if choice == "1":
                context.strategy = FirstStrategy()
            elif choice == "2":
                context.strategy = SecondStrategy()
            elif choice == "3":
                lis = use_strategy(lis, context)
            elif choice == "4":
                pos = input_int("position to remove")
                lis.remove(pos)
            elif choice == "5":
                a, b = input_int_range()
                lis.remove_in_range(a,b)
            elif choice == "6":
                k = input_int("input k to perform transform method with current list")
                lis = LinkedList.transform(lis, k)
            elif choice == "7":
                print(lis)

        except:
            e = sys.exc_info()[1]
            print("Error: ", str(e))
            continue

        if choice == "8":
            exit()
        else:
            continue

def use_strategy(lis, context):
    if isinstance(context.strategy, FirstStrategy):
        n = input_non_negative_int("input number of elements to generate: ")
        a, b = input_int_range()
        pos = input_non_negative_int("input pos: ")
        lis = context.execute_strategy(lis, pos, n, a, b)
    elif isinstance(context.strategy, SecondStrategy):
        f = Validation.validate_file_name(input("input file name to read from: "), "json")
        pos = input_non_negative_int("input pos: ")
        lis = context.execute_strategy(lis, pos, f)
    else:
        raise ValueError("context strategy is not valid, try to initialize it")
    return lis

# main
menu()
