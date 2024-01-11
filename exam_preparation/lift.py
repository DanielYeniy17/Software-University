def lift_func(waiting_people, train):
    for i in range(len(train)):
        if waiting_people > 3:
            current_people = abs(4 - int(train[i]))
            waiting_people -= current_people
            train[i] += current_people
        else:
            train[i] += waiting_people
            waiting_people = 0
    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(train) != len(train) * 4:
        print(f"The lift has empty spots!")

    return ' '.join([str(num) for num in train])


waiting_people = int(input())
train = list(map(int, input().split(' ')))
print(lift_func(waiting_people, train))
