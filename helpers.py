#function to input valid integer
def input_int(text):
    n=input("enter integer {} \n".format(text))
    try:
        n=int(n)
    except:
        print("you didn't enter an integer, try again")
        return input_int(text)
    return n

def is_in_range(num, a, b):
    if(a<=b):
        return num<=b and num>=a
    return False


def input_int_in_range(text, a,b):
    n = input("enter integer {} \n".format(text))
    try:
        n = int(n)
        if not is_in_range(a,b):
            print("you entered number that is not in range [", a,",",b,"]")
            return input_int_in_range(text)
    except:
        print("you didn't enter an integer, try again")
        return input_int_in_range(text)
    return n

#function to simplify entering valid integer
def input_positive_int(text):
    n=input("enter positive integer {} \n".format(text))
    try:
        n=int(n)
        if n<=0:
            print("you entered number that is less than or equal to zero")
            return input_positive_int(text)
    except:
        print("you didn't enter an integer, try again")
        return input_positive_int(text)
    return n

#function to simplify entering valid integer
def input_non_negative_int(text):
    n=input("enter non negative integer {} \n".format(text))
    try:
        n=int(n)
        if n<0:
            print("you entered number that is less than zero")
            return input_positive_int(text)
    except:
        print("you didn't enter an integer, try again")
        return input_positive_int(text)
    return n

def print_matrix(matrix):
    n= len(matrix)
    if n!= 0:
        m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],"\t", sep="", end="")
        print("")


def input_int_range():
    print("[a,b]")
    a=input_int("a (a<=b)")
    b=input_int("b (a<=b)")
    if a>b:
        print("a>b, try again")
        return input_int_range()
    return a,b