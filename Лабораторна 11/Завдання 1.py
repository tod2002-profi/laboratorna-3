# Lab 11

# Task 1
# Variant 6



from math import pi


class TCirle:
    def __init__(self, radius1, radius2):
        self.radius1 = radius1
        self.radius2 = radius2

    def squa(self):
        return pi * self.radius1 ** 2

    def len(self):
        return 2 * pi * self.radius1

    def __gt__(self):
        return self.radius1 > self.radius2

    def __add__(self):
        return self.radius1 + self.radius2

    def __sub__(self):
        return self.radius1 - self.radius2

    def __mul__(self, other):
        return self.radius1 * self.radius2 * other


a = int(input("Введіть перший радіус: "))
b = int(input("Введіть другий радіус: "))
d = int(input("Введіть число на яке потрібно множити:"))
print("R1 = {0}, R2 = {1}".format(a, b))
c = TCirle(a, b)
s = c.squa()
l = c.len()
poriv = c.__gt__()
sum = c.__sub__()
diff = c.__sub__()
mul = c.__mul__(d)
print("Площа круга = {0}".format(round(s)) + "\n" + "Довжина круга = {0}".format(round(l)) + "\n" + "Comporition = {0}".format(
    poriv) + "\n" + "Додавання = {0}".format(sum) + "\n" + "Різниця = {0}".format(diff) + "\n" + "Множення = {0}".format(mul))