word = input().split(' ')
search = input()
palindrome = []

for i in word:
    if i == ''.join(reversed(i)):
        palindrome.append(i)
print(f'{palindrome}')
print(f'Found palindrome {palindrome.count(search)} times')
