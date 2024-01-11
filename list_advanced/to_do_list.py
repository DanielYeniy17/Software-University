list = []

while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    priority = int(command[0])
    note = command[1]
    list.append((priority, note))

sorted_tasks = [data[1] for data in sorted(list)]

print(sorted_tasks)
