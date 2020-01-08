# Lab 10
# Task 1
# Variant 6



class Arefmetic:
    def __init__(self, first, diference, n):
        self.first = first
        self.diference = diference
        self.n = n
    def progres(self):
        return self.first + self.diference * (self.n - 1)
    def sum_progres(self):
        return ((2 * self.first + self.diference * (self.n - 1)) / 2) * self.n
b = int(input("Ведіть перший член арифметичної  прогресії: "))
print(b)
c = int(input("Введіть різницю прогресії:"))
print(c)
d = int(input("Введіть який член потрібно знайти:"))
print(d)
a = Arefmetic(b, c, d)
print("Знаходження {0} члена прогресії: {1}".format(d, a.progres()))
print("Знаходження суми {0} перших членів прогресії: {1}".format(d, a.sum_progres()))