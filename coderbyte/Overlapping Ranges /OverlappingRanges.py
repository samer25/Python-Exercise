def OverlappingRanges(arr):
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    x = arr[4]

    first = set()
    second = set()
    for i in range(a, b + 1):
        first.add(i)

    for i in range(c, d + 1):
        second.add(i)
    # code goes here

    if len(first & second) >= x or len(second & first) >= x:
        return True
    return False


# keep this function call here
print(OverlappingRanges(input()))
