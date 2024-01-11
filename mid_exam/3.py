storage = list(map(str, input().split(', ')))
while True:
    command = list(map(str, input().split(' - ')))
    if command[0] == 'End':
        break

    if command[0] == 'Add':
        if command[1] in storage:
            pass
        else:
            storage.append(command[1])
    elif command[0] == 'Remove':
        if command[1] in storage:
            storage.remove(command[1])
        else:
            pass
    elif command[0] == 'Bonus phone':
        list1 = list(map(str, command[1].split(':')))
        if list1[0] in storage:
            storage.append(list1[1])
        else:
            pass
    elif command[0] == 'Last':
        if command[1] in storage:
            storage.append(storage.pop(0))
        else:
            pass

print(', '.join(map(str, storage)))
