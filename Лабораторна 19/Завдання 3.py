
def recur(a):
    if a ==0:
        return 0
    elif a == 1:
        return 9
    else:
        return 2*recur(a-1) +3* recur(a-2)


n = int(input("n= "))
a = recur(n)
print(a)