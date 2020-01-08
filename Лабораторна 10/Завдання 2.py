
# Lab 10
# Task 2
# Variant 6

import datetime

class Student:
	def __init__(self,name,birthday, date, rating, scholarship_size):
		self.name = name
		self.bithday = birthday
		self.date = date
		self.rating = rating
		self.scholarship_size = scholarship_size
	def averenge(self):
		return sum(self.rating) / len(self.rating)
	def age(self):
		m = datetime.datetime.now()
		return m.year - self.bithday
	def end(self, g):
		return self.date + 5


b = input("Введіть імя: ")
c = int(input("Рік народження: "))
d = int(input("Рік вступу: "))
h = int(input("Скільки років залишилось навчатись: "))
j = int(input("Розмір стипендії"))
t = [] # Бали
v = [i for i in input("Ввести предмет: ").split()]
for i in v:
	n = int(input("Введіть оцінку за {0}: ".format(i)))
	t.append(n)
print(v, t)
a = Student(b, c, d, t, j)
i = a.averenge()
print("Середня арифметична оцінка: {0}".format(round(i)))
for iy in range(len(t)):
	if t[iy] < i:
		print(v[iy] +": " +str(t[iy]))
print("Вік: {0}" .format(a.age()))
print("В якому році ви закінчете: {0}" .format(a.end(h)))


