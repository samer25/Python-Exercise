capacity = 255
tank = 0
n = int(input())
for i in range(1, n + 1):
    litters = int(input())

    if tank + litters > capacity:
        print('Insufficient capacity!')
    else:
        tank += litters

    if n == i:
        print(tank)

