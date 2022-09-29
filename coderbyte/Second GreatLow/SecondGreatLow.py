def SecondGreatLow(arr):
    min_num = min(arr)
    max_num = max(arr)
    arr.remove(min_num)
    arr.remove(max_num)

    if len(arr) <= 0:
        return f'{max_num} {min_num}'
    else:
        for i in range(arr.count(max_num)):
            arr.remove(max_num)
        for i in range(arr.count(min_num)):
            arr.remove(min_num)

        min_num = min(arr)
        max_num = max(arr)
        return f'{min_num} {max_num}'
    # code goes here
