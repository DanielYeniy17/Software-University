command = list(map(str, input().split('||')))
fuel = int(input())
ammunition = int(input())
light_years = 0
for i in range(len(command)):
    list1 = list(map(str, command[i].split(' ')))

    if list1[0] == 'Travel':
        if light_years <= fuel:
            light_years = int(list1[1])
            fuel -= light_years
            print(f'The spaceship travelled {light_years} light-years.')
        elif light_years > fuel:
            print('Mission failed.')
            break
    elif list1[0] == 'Enemy':
        enemy = int(list1[1])
        if ammunition >= enemy:
            ammunition -= enemy
            print(f'An enemy with {enemy} armour is defeated.')
        elif ammunition < enemy:
            fuel -= 2 * enemy
            if fuel >= 0:
                print(f'An enemy with {enemy} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break
    elif list1[0] == 'Repair':
        fuel += int(list1[1])
        ammunition += int(list1[1])
        print(f'Ammunitions added: {int(list1[1]) * 2}.')
        print(f'Fuel added: {int(list1[1])}.')
    elif command[-1] == 'Titan':
        print('You have reached Titan, all passengers are safe.')
        break
