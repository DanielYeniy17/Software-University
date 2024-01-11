while True:
    text = input()
    if text == 'End':
        break
    if text == 'SoftUni':
        continue
    else:
        print(enumerate(text))
