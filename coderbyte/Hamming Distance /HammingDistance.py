def HammingDistance(strArr):
    first = strArr[0]
    second = strArr[1]
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1

    # code goes here
    return count


# keep this function call here
print(HammingDistance(["coder", "codec"]))
