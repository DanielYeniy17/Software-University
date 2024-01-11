element = input().split(" ")
bakery = {}
for i in range(0, len(element), 2):
    key = element[i]
    value = element[i + 1]
    bakery[key] = int(value)

search = input().split(' ')
for product in search:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
