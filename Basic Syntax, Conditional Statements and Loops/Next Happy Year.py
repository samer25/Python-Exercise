year = int(input())
n = 1
while True:
    year_in_str = str(year + n)
    if len(set(list(map(int, year_in_str)))) != len(year_in_str):
        n += 1
    else:
        print(year_in_str)
        break
