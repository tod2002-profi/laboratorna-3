# Lab 7
# Variant 6
# Task 2

# Побудувати прямокутно матрицю A еленти якої  задаються формулою:aij = i(sin(ix) + cos(jx)), i=1,N, j = 1,M
# Обчислити добуток елементів, добуток індексів яких менший за задане число х


from math import sin, cos
n = int(input("Кількість стовпців = "))
m = int(input("Кількість рядків = "))
x = int(input("x = "))


def a_i_j(i, j, x):
    a = i * (sin(i * x) + cos(j * x))
    return a


A = [[a_i_j(i, j, x)for i in range(1, n + 1)]for j in range(1, m + 1)]
for i in A:
    print(i)








