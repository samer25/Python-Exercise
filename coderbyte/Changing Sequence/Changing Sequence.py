def ChangingSequence(arr):
    index = -1
    for i in range(1, len(arr) - 1, 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1] or \
                arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
            index = i
    return index


# keep this function call here
print(ChangingSequence([1, 2, 4, 6, 4, 3, 1]))
