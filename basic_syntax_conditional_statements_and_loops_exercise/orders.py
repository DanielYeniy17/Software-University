orders = int(input())
total = 0
for i in range(orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 > price > 100:
        continue
    elif 1 > days > 31:
        continue
    elif 1 > capsules > 2000:
        continue
    one = price * days * capsules
    total += one
    if total != 0:
        print(f'The price for the coffee is: ${one:.2f}')
print(f'Total: ${total:.2f}')
