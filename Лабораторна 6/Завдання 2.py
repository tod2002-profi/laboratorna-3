
# Lab 6
# Task 2
# Variant 6
# Елементи масиву A = ai   задаються так: ai = 1!*sin b+2!*sin 2b + ... i! sin ib (1,2...n)
# Знайти min(a1*a2,a2*a3,a3*a4,...,an-1*an)

import math
import functools
n = int(input("n = "))
b = float(input("b = "))
def get_a(i):
	z = 1
	# r = 1
	s = 0
	for j in range(i):
		s = s+math.factorial(z) * math.sin(z * b)
		z = z+1
		# z = z * r
	return s
A = []



for i in range(1, n+1):
	A.append(get_a(i) * get_a(i+1))

# a = [get_a(i) for i in range(1,i+1)]

# j = 0

# while j < i:
m = min (A)

	# j = j+1
print('min = ', m)

