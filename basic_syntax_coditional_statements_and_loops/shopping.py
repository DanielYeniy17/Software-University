budget = int(input())
condition = True
all_products = 0
while condition:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    product = int(command)
    all_products += product
    if all_products > budget:
        condition = False
        print('You went in overdraft!')
        break
