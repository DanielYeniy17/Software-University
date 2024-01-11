number_cities = int(input())
whole_price = 0
for i in range(number_cities):
    city = input()
    income = float(input())
    outcome = float(input())

    if i % 2 == 0 and i % 4 != 0 and i != 0:
        outcome += (0.5 * outcome)

    elif i % 4 == 0 and i != 0:
        income -= income * 0.1

    money = income - outcome
    whole_price += money
    print(f'In {city} Burger Bus earned {money:.2f} leva.')

print(f'Burger Bus total profit: {whole_price:.2f} leva.')
