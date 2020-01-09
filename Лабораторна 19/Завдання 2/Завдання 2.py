with open('fail.txt') as f:
    list_a = []
    for line in f:
        list_a.append(int(line))
    print(list_a)
    b = [x for x in list_a if x < 0]
    print(max(b))
with open('V.dat.txt', 'w') as g:
    for i in b:
        g.write(str(i)+'\n')