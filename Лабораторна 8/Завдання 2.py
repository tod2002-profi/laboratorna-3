# Використовуючи підпрограму визначення перпендикулярності двох прямих на площині, визначити, скільки взаємно перпендикулярних пар прямих є серед вказаних n прямих:  .
from math import sqrt


def perpendukylar(A1, A2, B1, B2):
    Skalar = A1 * A2 + B1 * B2  # Скалярний добуток
    if Skalar == 0:
        return 1
    else:
        return 0


count = 0#К-сть взаємно перпендикулярних пар
n = int(input("Ввести к-сть n: "))
A = [int(input("Ввести А: ")) for i in range(n)]
B = [int(input("Ввести B: ")) for j in range(n)]
for i in range(n):
    if i + 1 < n:
        c = perpendukylar(A[i], A[i + 1], B[i], B[i + 1])
        count += c
print("К-сть пар: {0}".format(count))