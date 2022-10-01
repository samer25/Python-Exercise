def LargestPair(num):
    num = str(num)

    l = [int(num[x] + num[x+1]) for x in range(len(num)-1)]
    # for i in range(len(num) - 1):
    #     l.append(int(num[i] + num[i + 1]))
    # code goes here
    return max(l)


# keep this function call here
print(LargestPair(4759472))
