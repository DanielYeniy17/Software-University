text = input()
vowels = ['a', 'e', 'u', 'o', 'i', 'A', 'E', 'U', 'O', 'I']
no_vowels = ''.join([x for x in text if x not in vowels])
print(no_vowels)
