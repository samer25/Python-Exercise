def Superincreasing(arr):
    sums = 0
    for i in range(len(arr)):
        if arr[i] > sums:
            sums += arr[i]
        else:
            return False
    return True
    # code goes here


# keep this function call here
print(Superincreasing([1, 3, 6, 13, 54]))
