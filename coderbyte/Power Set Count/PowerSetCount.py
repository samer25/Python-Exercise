from itertools import combinations


def PowerSetCount(arr):
    count = 0
    for i in range(len(arr)):
        count += len(list(combinations(arr, i + 1)))
    # code goes here
    return count + 1


# keep this function call here
print(PowerSetCount([5, 6, 1, 3]))
