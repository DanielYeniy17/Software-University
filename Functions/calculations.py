function = input()
num1 = int(input())
num2 = int(input())


def solution():
    if function == 'multiply':
        return int(num1 * num2)
    elif function == 'divide':
        return int(num1 / num2)
    elif function == 'add':
        return num1 + num2
    elif function == 'subtract':
        return num1 - num2


print(solution())
