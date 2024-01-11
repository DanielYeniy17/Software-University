
def create_plants(plants, number):
    for i in range(number):
        flower = input().split('<->')
        flower_name = flower[0]
        rarity = int(flower[1])

        if flower_name not in plants:
            plants[flower_name] = {'rarity': rarity, 'rating': []}

        else:
            plants[flower_name]['rarity'] += rarity

    return plants


def additional_plant(plants):
    while True:
        command = input().split(': ')
        if command[0] == 'Exhibition':
            break

        data = command[1].split(' - ')
        type_command = command[0]
        plant = data[0]

        if plant not in plants:
            print('error')
            continue

        if type_command == 'Rate':
            rating = int(data[1])
            plants[plant]['rating'].append(rating)

        elif type_command == 'Update':
            new_rarity = int(data[1])
            plants[plant]['rarity'] = new_rarity

        elif type_command == 'Reset':
            plants[plant]['rating'].clear()

    return plants


def print_func(plants):
    print('Plants for the exhibition:')

    for dic_el in plants:
        if len(plants[dic_el]['rating']) > 0 and sum(plants[dic_el]['rating']) > 0:
            average_rating = sum(plants[dic_el]['rating']) / len(plants[dic_el]['rating'])
        else:
            average_rating = 0
        rarity = plants[dic_el]['rarity']
        print(f"- {dic_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plants_list(number):
    plants = {}

    create_plants(plants, number)
    additional_plant(plants)
    print_func(plants)


n = int(input())
plants_list(n)
