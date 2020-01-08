# Lab 7
# Variant 6
# Task 3

#Дано матрицю А і ветор в .Знайти вектор вА


n = int(input("Кількість рядків : "))
m = int(input("Кількість стовпців: "))
matrix = [[int(input("Element[{0}][{1}]= ".format(i, j))) for j in range(m)] for i in range(n)]
for i in matrix:
    print(i)
vec = [int(input("Елемент вектора: ")) for i in range(m)]
print("Старий вектор= " + str(vec))
answer = []
s = 0
matrixt = list(zip(*matrix)) #Створюємо транспоновану матрицю
k = -1
for i in range(m):
    k += 1
    if k == m:
        break
    for j in range(n):
        s += vec[k] * matrixt[i][j]
    answer.append(s)
    s = 0

print("Новий вектор = {0}".format(answer))







