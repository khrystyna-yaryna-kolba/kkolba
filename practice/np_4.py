from linked_list import *
from random_generator import *
from random_iterator import *
def entering_list():
    choice = input("enter your choice \n 1 - random generating \n 2 - manual input \n 3- (return []) \n")
    if choice=="1":
        N=input_non_negative_int("N - length of list")
        a,b = input_int_range()
        lis = LinkedList.random_generating(N,a,b)
        return lis
    elif choice=="2":
        N=input_non_negative_int("N")
        lis=LinkedList.input_int_list(N)
        return lis
    elif choice=="3":
        return LinkedList()
    else:
        return entering_list()



def menu():
    lis = LinkedList()
    while True:
        #lis.print()
        choice = input("enter your choice \n 1 - tranform \n 2 - enter list(random or input) \n 3 - insert \n 4 - remove "
                       "\n 5 - generate random numbers in range with generator \n 6 - generate random numbers in "
                       "range with iterator \n 7 - print list \n 8 - exit \n")
        if choice == "1":
            k = input_int("k")
            result = LinkedList.transform(lis, k)
            print("list:")
            lis.print()
            print("transformed list:")
            result.print()
        elif choice == "2":
            lis = entering_list()
            continue
        elif choice == "3":
            pos = input_int("position to insert")
            data = input_int("data to insert")
            lis.insert(pos,data)
        elif choice == "4":
            pos = input_int("position to remove")
            lis.remove(pos)
        elif choice == "5":
            lis = LinkedList()
            n = input_non_negative_int("num of generated numbers")
            a, b = input_int_range()
            generator = random_generator(n, a, b)
            print("using generator...")
            for i in generator:
                print(i)
                lis.append(i)
            #lis.print()
        elif choice == "6":
            lis = LinkedList()
            n = input_non_negative_int("num of generated numbers")
            a, b = input_int_range()
            it = RandomIterator(n, a, b)
            iterator = iter(it)
            print("using iterator...")
            for i in iterator:
                print(i)
                lis.append(i)
            #lis.print()
        elif choice == "7":
            lis.print()
        elif choice == "8":
            exit()
        else:
            continue

"""Задано масив з N цілих чисел. Сформувати масив таким чином, щоб спочатку були всі від’ємні
     елементи масиву, потім додатні і, після них нульові, зберігши порядок. Якщо якоїсь групи
      чисел не існує, то після кожного числа, що дорівнює K вставити рандомне число х цієї
       групи. Наприклад, -5 0 -4 0 -5 -6 0. K= -5. Немає додатних чисел. -5 7 -4 -5 6 -6 0 0 0.
        Числа 7 і 6 - рандомні, після кожного -5.
"""
# main
menu()
