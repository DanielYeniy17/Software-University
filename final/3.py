heroes = {}

while True:
    command = input().split(' ')
    if command[0] == 'End':
        break

    if command[0] == 'Enroll':
        name = command[1]

        if name not in heroes:
            heroes[name] = []
        else:
            print(f'{name} is already enrolled.')
            continue
    elif command[0] == 'Learn':
        hero = command[1]
        spell_name = command[2]
        if hero in heroes:
            if spell_name not in heroes[hero]:
                heroes[hero].append(spell_name)
            else:
                print(f'{hero} has already learnt {spell_name}.')
        else:
            print(f"{hero} doesn't exist.")
    elif command[0] == 'Unlearn':
        name = command[1]
        spell_name = command[2]
        if name in heroes:
            if spell_name not in heroes[name]:
                print(f"{name} doesn't know {spell_name}.")
            else:
                heroes[name].remove(spell_name)

        else:
            print(f"{name} doesn't exist.")


print(f"Heroes:")
for keys, values in heroes.items():
    if not values:
        values = ''
    else:
        values = values.pop()
    print(f"== {keys}: {values}")


