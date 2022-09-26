from kkolba.helpers import *

def create_matrix(n):
    import numpy as np
    matrix = np.zeros((n,n), dtype = int)
    n = len(matrix)
    range_helper = list(range(1,n+1))
    for i in range(n):
        matrix[i][:n-i] = range_helper[i:]

    return matrix


def menu():
    choice = input("enter your choice \n 1 - create matrix \n 2 - exit \n")
    if choice == "1":
        n = input_positive_int("n")
        print_matrix(create_matrix(n))
    elif choice=="2":
        exit()
    else:
        return menu()
    return menu()


"""Утворити квадратну матрицю порядку n :

 1   2 3 4 ...  n
 2   3 4 5... n 0 
 3   4 5 .. n 0 0
 ...
 n-1 n 0 .. 0 0 0
 n   0 0 .. 0 0 0

"""
#main
menu()