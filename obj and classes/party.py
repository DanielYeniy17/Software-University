class Party:

    def __init__(self):
        self.people = []


party = Party()

queue = input()
while queue != 'End':
    party.people.append(queue)
    queue = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
