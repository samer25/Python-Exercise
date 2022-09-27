party_size = int(input())
days = int(input())

earnings = 0


for i in range(1, days + 1):
    earnings += 50
    earnings -= party_size * 2
    earnings_per_party = earnings // party_size

    if i % 10 == 0:
        party_size -= 2

    if i % 15 == 0:
        party_size += 5

    if i % 3 == 0:
        earnings -= party_size * 3

    if i % 5 == 0:
        earnings += 20 * party_size
        if i % 3 == 0:
            earnings -= party_size * 2

        # earnings -= earnings / party_size * 2

print(f'{party_size} companions received {earnings // party_size} coins each.')
