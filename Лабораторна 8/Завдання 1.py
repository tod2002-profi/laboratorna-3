from math import factorial, cos, sqrt, sin
#За даними дійсними числами a і b  обчислити

def get_f(x):
    if x < 0:
        count = 0
        for i in range(1, 9):
            count += 1 + (x / factorial(i))
        return count
    if 0 <= x <= 5:
        return 15 + sqrt(cos(x) ** 6)
    if x > 5:
        return min([1, 2 * sin(x)])


a = int(input("Ввести число= "))
b = int(input("Ввести число= "))
u = max(get_f(a),get_f(b))-get_f(3)
print("Відповідь = {0}".format(round(u)))