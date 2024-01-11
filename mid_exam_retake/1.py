cost = float(input())
months = int(input())
saved_money = 0
for i in range(months):

    if i % 2 == 0 and i != 1 and i != 0:
        saved_money -= saved_money * 0.16
    elif i % 3 == 0 and i != 0:
        saved_money += saved_money * 0.25

    saved_money += cost * 0.25

result = abs(saved_money - cost)

if saved_money > cost:
    print(f"Bravo! You can go to Disneyland and you will have {result:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {result:.2f}lv. more.")
