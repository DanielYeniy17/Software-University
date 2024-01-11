first = int(input())
second = int(input())
string = ''
for i in range(first, second + 1):
    string += chr(i) + " "
print(string)
