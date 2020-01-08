# Lab 6
# Task 1
# Variant 6
# Дано n дійсних чисел: X1,X2.....Xn. Знайти найменше серед  додатних


import functools

n = int(input("n = "))

nums = [float(input("x({0}) = ".format(i))) for i in range(n)]





nums_to_remove = []
for num in nums:
    if num < 0:
        nums_to_remove.append(num)
for num in nums_to_remove:
        nums.remove(num)



smallest = min(nums);



print(smallest);
