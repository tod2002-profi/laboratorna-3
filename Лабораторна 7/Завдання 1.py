# Lab 7
# Variant 6
# Task 1

# Визначити суму додатних елементів матриці з непарною сумою індексів.


n = int(input("n = "))
m = int(input("m = "))

matrix = [
    [int(input("mat[{0}][{1}] = ".format(i,j))) for j in range(m)] for i in range(n)
]

product = 0


for i in range(0, n):
    for j in range(0, m):

        if matrix[i][j] > 0 and (i + j)% 2 == 1:
            product += matrix[i][j]

print(product)







