x = int(input())
y = int(input())

l = [i * x for i in range(y + 1) if i != 0]

print(l)
