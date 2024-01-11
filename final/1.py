spell = input()

while True:
    command = input().split(" ")

    if command[0] == 'Abracadabra':
        break
    if command[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif command[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif command[0] == 'Illusion':
        index = int(command[1])
        letter = command[2]
        if index <= len(spell):
            spell = spell.replace(spell[index], letter)
            print('Done!')
        else:
            print('The spell was too weak.')
    elif command[0] == 'Divination':
        substring_one = command[1]
        substring_two = command[2]
        if substring_one in spell:
            spell = spell.replace(substring_one, substring_two)
            print(spell)
        else:
            print('The spell was too weak.')

    elif command[0] == 'Alteration':
        substring = command[1]
        substitute = ''
        if substring in spell:
            spell = spell.replace(substring, substitute)
            print(spell)
        else:
            continue
    else:
        print('The spell did not work!')
