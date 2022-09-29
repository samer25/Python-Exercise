def MeanMode(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    mode = max(dic, key=dic.get)
    mean = sum(arr) / len(arr)
    # code goes here
    return int(mode == mean)


print(MeanMode([1, 2, 3]))