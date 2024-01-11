words = input().split(" ")
names = {}
for word in words:
    lower_words = word.lower()
    if lower_words not in names:
        names[lower_words] = 0
    names[lower_words] += 1

for key, value in names.items():
    if value % 2 != 0:
        print(key, end=" ")
