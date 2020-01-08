# Lab 6
# Task 4
# Variant 6
# Перетворити масив таким чином, щоб спочатку розміщувалися всі елементи рівні 0 ,а потім  всі інші
def quick_sort(a):
    j = 0
    for i in range(len(a)):
        if a[i] >= 0:
            if i != j:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
            j += 1

    return a

n = int(input("n = "))

base = [float(input("#{0} = ".format(i))) for i in range(n)]

#
a1 = list(filter(lambda x: x == 0, base))
a2 = list(filter(lambda x: x != 0, base))
result = a1+a2
print( "Відфільтрований список: ", result)

print("Заданий список: ", base)
# print("Generators: ", generators_solution)
# print("Quick sort: ", quick_sort(base))