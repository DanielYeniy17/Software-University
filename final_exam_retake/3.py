bands = {}
time = {}
total_time = 0
while True:
    command = input().split('; ')
    if command[0] == 'Start!':
        break

    if command[0] == 'Add':
        band = command[1]
        names = command[2]
        if band in bands:
            if names in bands[band]:
                continue
            else:
                bands[band] += names
        else:
            bands[band] = names
    elif command[0] == 'Play':
        band = command[1]
        time_1 = int(command[2])
        time[band] = time_1
        total_time += time_1

print(f"Total time: {total_time}")
for key, value in time.items():
    print(f"{key} -> {value}")
for key, value in time.items():
    print(key)
    print(f"=> ")