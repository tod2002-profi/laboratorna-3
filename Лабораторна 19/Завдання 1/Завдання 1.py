with open("fail.txt", "r") as f:
    s = 0
    item = 0
    lin = f.readlines()
    print(lin)
    for i in lin:
        s += int(i)
        item += 1
print(s, item)

with open("fail1.txt", 'w') as a:
    a.write(str(s / item))
    