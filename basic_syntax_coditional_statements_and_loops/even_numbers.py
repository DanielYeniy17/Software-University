n = int(input())
even = 0
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        print(f'{num} is odd!')
        break
    else:
        even += 1
        continue
if even == n:
    print('All numbers are even.')
