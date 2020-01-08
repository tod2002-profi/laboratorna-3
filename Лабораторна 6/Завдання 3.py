# Lab 6
# Task 3
# Variant 6
import functools
#Дано 2 вектори x,yєR^n . Зясувати , чи паралельні вони
def make_vector(name, n):
    return [float(input("{0}({1}) = ".format(name, i+1))) for i in range(n)]

n = int(input("n = "))

v1 = make_vector("v1", n)
v2 = make_vector("v2", n)

a = list(map(lambda c1,c2: c1 / c2, v1, v2))

def all_the_same(a):
    return len(set(a)) in (0, 1)

if len(set(a)) == 1:
    print("Вектори паралельні")
else:
    print("Вектори не паралельні")




