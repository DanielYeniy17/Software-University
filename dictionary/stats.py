bakery = {}
while True:
    command = input()
    if command == 'statistics':
        break

    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product not in bakery:
        bakery[product] = 0
    bakery[product] += quantity

print('Products in stock:')
for (product, quantity) in bakery.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')
