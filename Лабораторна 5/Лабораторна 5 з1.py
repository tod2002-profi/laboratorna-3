# Lab 5
# variant 6
# Output (2^2+4^2+...+(2n)^2)+(3^3+5^3+...(2n+1)^3

import math

n = int(input("n = "))


S = 0

for i in range(1, n+1):
    S+= ((2*i)**2)+((2*i+1)**3)
print("S = {0}".format(S))
