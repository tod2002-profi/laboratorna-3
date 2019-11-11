import math
x1 = int(input('Введіть значення x для точки A: '))
y1 = int(input('Введіть значення y для точки A: '))
x2 = int(input('Введіть значення x для точки B: '))
y2 = int(input('Введіть значення y для точки B: '))
x3 = int(input('Введіть значення x для точки C: '))
y3 = int(input('Введіть значення y для точки C: '))
AB = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
BC = math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
AC = math.sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
if AB == BC or AB == AC:
    print ( " Трикутник ABC рівностороній " )
else:
    print ( " Трикутник ABC НЕ рівностороній " )