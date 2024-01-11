

def calculation():
    price = 0
    if product == 'coffee':
        price = 1.50
    elif product == 'coke':
        price = 1.40
    elif product == 'water':
        price = 1
    elif product == 'snacks':
        price = 2
    result1 = price * n
    return f'{result1:.2f}'



product = input()
n = int(input())


print(calculation())
