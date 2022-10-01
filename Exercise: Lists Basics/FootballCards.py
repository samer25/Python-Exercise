a = [x for x in range(1, 12)]
b = [x for x in range(1, 12)]

input_code = input().split(' ')
cards = [x.split('-') for x in input_code]

for card in cards:
    if card[0] == 'A':
        if int(card[1]) in a:
            a.remove(int(card[1]))
    elif card[0] == 'B':
        if int(card[1]) in b:
            b.remove(int(card[1]))

    if len(a) < 7 or len(b) < 8:
        print(f'Team A - {len(a)}; Team B - {len(b)}')
        print('Game was terminated')
        break

else:
    print(f'Team A - {len(a)}; Team B - {len(b)}')
