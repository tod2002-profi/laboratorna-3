# Lab 7
# Variant 6
# Task 6
# Дана числова прямокутна матриця.Визначити номера рядків і стовпців всіх сідлових точок матриці, матриця А має  сідлову точку А0 якщо Аij є мінімальним елементом в і-у рядку і максимальним в j-у стовпці
def saddle_point(matrix):
    if len(matrix) == 1:
        return 0
    y = 0
    while len(matrix) > y:
        for i in matrix:
            l_min = min(i)
            l_index = i.index(l_min)
            for j in matrix:
                if l_min > j[l_index]:
                    return matrix.index(i), l_index
        return None
    y += 1


b = saddle_point([[1, 850, -1], [1, 2, -2]])
print(b)







