def AdditivePersistence(num):
    num = str(num)
    count = 0
    while len(num) > 1:
        totalCount = 0
        for i in num:
            totalCount += int(i)
        count += 1
        num = str(totalCount)
    return count


# keep this function call here
print(AdditivePersistence(12345))
