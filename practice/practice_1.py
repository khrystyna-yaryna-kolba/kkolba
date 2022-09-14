"""8. Перестановкою P [1..n] розміру n називається набір чисел від 1 до n,
 розташованих в певному порядку. При цьому в ньому мають бути присутні рівно
  один раз кожне з цих чисел. Прикладом перестановок є 1, 3, 4, 5, 2 (для n = 5)
   і 3, 2, 1 (для n = 3), а, наприклад, 1, 2, 3, 4, 5, 1 перестановкою не є, так
   як число 1 зустрічається два рази. Число i називається нерухомою точкою для
    перестановки P, якщо P[i] = i. Наприклад, в перестановці 1, 3, 4, 2, 5
    рівно дві нерухомих точки: 1 і 5, а перестановка 4, 3, 2, 1 не має
    нерухомих точок.
Дано два числа: n та k. Знайдіть кількість перестановок
 розміру n з рівно k нерухомими точками.
Вхідні дані
Ввести з клавіатури два цілих числа n (1 ≤ n ≤ 9) і k (0 ≤ k ≤ n).
Вихідні дані
Вивести на екран відповідь на задачу.
"""

#input
n = input("input integer n (1 ≤ n ≤ 9) \n")
k = input("input integer k (0 ≤ k ≤ n) \n")

def check_input(n, k):
    try:
        if not (n.isdigit() and k.isdigit()):
            raise ValueError("n and k should be integers")
        n=int(n)
        k=int(k)
        if n<1 or n>9:
            raise ValueError("n is out of range")
        elif k<0 or k>n:
            raise ValueError("k is out of range")
        return n, k
    except ValueError as e:
        print(e, ", check your input and try again")
        exit()


n, k = check_input(n, k)

#functions
#first version
def static_permutations(n, k):
    from itertools import permutations
    ans = 0
    perm = permutations(range(1,n+1))
    for i in perm:
        count=0
        for j in range(n):
            if i[j]==j+1:
                count+=1
        if count==k:
            ans+=1
    return ans


#second version
def mathem_permutes(n, k):#derangements
    import math
    c = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    subfactorial = 0
    for i in range(n-k+1):
        subfactorial= subfactorial + int(((-1)**i)*math.factorial(n-k)/math.factorial(i))
    return int(c*subfactorial)

#printing answer
#brute force
print(static_permutations(n, k))

#the best,mathematical, but harder to understand
print(mathem_permutes(n, k))
