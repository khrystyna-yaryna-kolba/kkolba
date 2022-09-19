import random
#generating random list of length N with integer values in range [a, b]
def random_generating(N, a, b):
    list = []
    for i in range(N):
        list.append(random.randrange(a, b+1))
    return list

#manual input of list of integers of length N
def input_list(N):
    list = []
    for i in range(N):
        n = input_int("list[{}]".format(i))
        list.append(n)
    return list

#function to simplify entering valid integer
def input_int(text):
    n=input("enter integer {} \n".format(text))
    try:
        n=int(n)
    except:
        print("you didn't enter an integer, try again")
        return input_int(text)
    return n


#entering list using two different ways
def entering_list():
    while True:
        choice = input("enter your choice \n 1 - random generating \n 2 - manual input \n 3 - break and try again \n 4 - stop entering list (return []) \n")
        if choice=="1":
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
            lis=input_list(N)
            return lis
        elif choice=="4":
            return []
        else:
            continue



def tranform(list, k):
    negative = []
    positive = []
    zeros = []

    #filling three lists to maintain the order
    for i in list:
        if i<0:
            negative.append(i)
        elif i>0:
            positive.append(i)
        else:
            zeros.append(0)
    #checking if there is missing group, if yes, than what is that
    #(doesn't handle the situation when there are two missing groups, just chooses one)
    missing_group = None#-1, 0, 1
    if len(negative)==0:
        missing_group=-1
    elif len(positive)==0:
        missing_group=1
    elif len(zeros)==0:
        missing_group=0

    #helping function to create number of given group(negative, positive or zero)
    def get_group_num(group):
        if group>0:
            return random.randrange(1, 50)
        elif group<0:
            return random.randrange(-50, -1)
        else:
            return 0

    #inserting random elements of missing group after each k
    #(as in the instructions)
    if missing_group!=None:
        if k>0:
            for i in range(len(positive)):
                if positive[i]==k:
                    positive.insert(i+1, get_group_num(missing_group))
        elif k<0:
            for i in range(len(negative)):
                if negative[i]==k:
                    negative.insert(i+1, get_group_num(missing_group))
        else:
            for i in range(len(zeros)):
                if zeros[i]==k:
                    zeros.insert(i+1, get_group_num(missing_group))

    #concatenating parts to get final result
    result = negative + positive + zeros
    return result

"""Задано масив з N цілих чисел. Сформувати масив таким чином, щоб спочатку були всі від’ємні
 елементи масиву, потім додатні і, після них нульові, зберігши порядок. Якщо якоїсь групи
  чисел не існує, то після кожного числа, що дорівнює K вставити рандомне число х цієї
   групи. Наприклад, -5 0 -4 0 -5 -6 0. K= -5. Немає додатних чисел. -5 7 -4 -5 6 -6 0 0 0.
    Числа 7 і 6 - рандомні, після кожного -5.
"""
#main
list = entering_list()
k = input_int("k")
result=tranform(list, k)
print("list:",list)
print("transformed list:", result)
