


n = int(input("Введіть натуральне число: "))
m = 0

while n > 0:
    digit = n % 10 ;
    n = n // 10;
    m = m * 10
    m = m + digit

print('"Зворотнє число:', m)