import re


number = int(input())

for i in range(number):

    string = input()
    pattern = r'(\!{1}[A-Z][a-z]{3,}\!{1})(\:{1})(\[{1}[A-Z][A-Za-z]{8,}\]{1})'
    result = re.match(pattern, string)
    word = string.split(':')
    list_1 = []
    strings = {word[0]: list_1}
    if not result:
        print('The message is invalid')
        continue
    else:
        for ch in word[1]:
            if ch != '[' and ch != ']':
                strings[word[0]].append(ord(ch))

    for keys, values in strings.items():

        print(f"{keys}: {' '.split(values)}")

