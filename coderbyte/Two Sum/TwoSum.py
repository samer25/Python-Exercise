def TwoSum(arr):
    result = []
    for i in range(1, len(arr)):
        calc = arr[i]
        for j in range(i + 1, len(arr)):
            if calc + arr[j] == arr[0]:
                result.append(str(calc) + ',' + str(arr[j]))
                break

    # code goes here
    if result:
        return ' '.join([str(x) for x in result])
    else:
        return -1


# keep this function call here
print(TwoSum([7, 3, 5, 2, -4, 8, 11]))
