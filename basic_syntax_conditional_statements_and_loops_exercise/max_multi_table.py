num = int(input())
num1 = int(input())
max = 0
for i in range(num1, num, -1):
    if i % num == 0:
        max = i
        break
print(max)
