from math import ceil

people = int(input())
capacity = int(input())
sum = 0
if people <= capacity:
    sum = 1
    print(sum)
elif people > capacity:
    sum = people / capacity
    print(ceil(sum))
