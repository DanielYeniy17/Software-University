username = input()

while True:
    command = input().split(' ')
    if command[0] == 'Registration':
        break

    if command[0] == 'Letters':
        set = command[1]
        if set == 'Lower':
            username = username.lower()
        elif set == 'Upper':
            username = username.upper()
        print(username)

    elif command[0] == 'Reverse':
        start = int(command[1])
        end = int(command[2]) + 1
        new_username = username[start:end]

        print(new_username[::-1])

    elif command[0] == 'Substring':
        substring = command[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif command[0] == 'Replace':
        ch = command[1]
        username = username.replace(ch, '-')
        print(username)
    elif command[0] == 'IsValid':
        ch = command[1]
        if ch in username:
            print('Valid username.')
        else:
            print(f"{ch} must be contained in your username.")
