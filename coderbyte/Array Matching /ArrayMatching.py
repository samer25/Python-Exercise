def ArrayMatching(strArr):
    x = [int(i) for i in strArr[0][1:-1].split(',')]
    y = [int(i) for i in strArr[1][1:-1].split(',')]
    result = []
    if len(x) > len(y):
        x, y = y, x
    # code goes here
    for i in range(len(x)):
        result.append(x[i] + y[i])

    result += y[len(x)::]

    return '-'.join([str(x) for x in result])


# keep this function call here
print(ArrayMatching(["[1, 2, 5, 6]", "[5, 2, 8, 11]"]))
