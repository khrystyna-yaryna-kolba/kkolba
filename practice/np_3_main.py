from linked_list import *

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
    lis = entering_list()
    while True:
        lis.print()
        choice = input("enter your choice \n 1 - tranform \n 2 - return to creating list \n 3 - insert \n 4 - remove \n 5 - exit \n")
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
            data = input_int("data to insert)")
            lis.insert(pos,data)
        elif choice == "4":
            pos = input_int("position to remove")
            lis.remove(pos)
        elif choice == "5":
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
