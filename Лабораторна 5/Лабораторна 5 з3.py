import math

epsilon = float(input("epsilon = "))
x = float(input("x = "))

right = 1
left = math.cos(x)


n = 1

while True:

        y = ((((-1) ** n) * x ** (2 * n)) / math.factorial(2 * n))

        if y < epsilon:
                break
#
        right += y
        n += 1

print("y = {0}".format(y))
print("n = {0}".format(n))
print("right = {0}".format(right))
print("left = {0}".format(left))




