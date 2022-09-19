import random
#generating random list of length N with integer values in range [a, b]
def random_generating(N, a, b):
    list = []
    for i in range(N):
        list.append(random.randrange(a, b+1))
    return list

#manual input of list of integers of length N
def input_list(N):
    lis = []
    for i in range(N):
        n = input_int("list[{}]".format(i))
        lis.append(n)
    return lis

#function to simplify entering valid integer
def input_int(text):
    n=input("enter integer {} \n".format(text))
    try:
        n=int(n)
    except:
        print("you didn't enter an integer, try again")
        return input_int(text)
    return n


#bubble sort
def bubble_sort(arr):
    n = len(arr)
    initial_indexes = list(range(n))#to remember initial order in case we will need it
    num_of_swaps = 0
    num_of_comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                initial_indexes[j], initial_indexes[j + 1] = initial_indexes[j + 1], initial_indexes[j]#don't count this in steps because it's not about sorting but helping only
                num_of_swaps+=1
            num_of_comparisons+=1
    return num_of_swaps, num_of_comparisons, initial_indexes



#binary search
#return ( if exist , count of operations to complete that search )
def binary_search(lis, value):
    import math
    li=lis.copy()
    num_of_swaps, num_of_comparisons, initial_indexes  = bubble_sort(li)
    operations_count = 0 #operation is setting new values for variables
    #steps
    #1. find middle element
    #2. define new bound (or return result if middle element is element what we are looking for)
    #repeat from 1 till bounds are valid
    comparisons_count = 0 #comparison operations

    left = 0
    right = len(li) - 1
    middle = 0
    while left <= right:
        comparisons_count+=1
        middle = (left + right)//2
        operations_count+=1
        if li[middle]<value:
            comparisons_count+=1
            left = middle+1
            operations_count+=1
        elif li[middle]>value:
            comparisons_count+=2
            right = middle-1
            operations_count+=1
        else:
            comparisons_count+=2
            return initial_indexes[middle],operations_count,comparisons_count, num_of_swaps, num_of_comparisons
    comparisons_count+=1
    return False, operations_count,comparisons_count, num_of_swaps, num_of_comparisons

#entering list using two different ways
#interface
def entering_list():
    while True:
        choice = input("enter your choice \n 1 - random generating \n 2 - manual input \n 3 - (return []) \n")
        if choice=="1":
            N=input_int("N - length of list")
            while N<0:
                print("N should be greater than zero")
                N=input_int("N - length of list")
            while True:
                a=input_int("a (a<=b)")
                b=input_int("b (a<=b)")
                if a<=b:
                    break
                print("a>b, try again")
            lis = random_generating(N,a,b)
            return lis
        elif choice=="2":
            N=input_int("N")
            while N<0:
                print("N should be greater than zero")
                N=input_int("N - length of list")
            lis=input_list(N)
            return lis
        elif choice=="3":
            return []
        else:
            continue







#main
lis = entering_list()
while True:
    print(lis)
    choice = input("enter your choice \n 1 - binary search \n 2 - return to creating list \n 3 - exit \n")
    if choice=="1":
        val = input_int("val to search")
        existence, count,comparisons_count, num_of_swaps, num_of_comparisons = binary_search(lis, val)
        print("existence of given val in the list(index or False): {}".format(existence))
        print("number of steps to perform that search: {}".format(count))
        print("number of comparisons to perform that search: {}".format(comparisons_count))
        print("number of swaps to perform bubble sorting before binary search: {}".format(num_of_swaps))
        print("number of comparisons to perform bubble sorting before binary search: {}".format(num_of_comparisons))
    elif choice=="2":
        lis = entering_list()
        continue
    elif choice=="3":
        exit()
    else:
        continue
