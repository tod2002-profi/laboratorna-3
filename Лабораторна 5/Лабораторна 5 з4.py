Нехай X0 = 0, X1=X2=9,Xi=Xi-1+4Xi-3,X>=3, Визначити Xn
n = int(input("n = "))

i = 3

z0 = 0
z1 = 9
z2 = 9



x = 0

while not i == n+1:
	x = z2 + 4 * z0
	z0 = z1
	z2 = x
	i += 1



print("Xn = {0}".format(x))


