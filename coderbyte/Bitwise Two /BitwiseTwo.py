def BitwiseTwo(strArr):
    s = ''
    for i in range(len(strArr[0])):
        s += str(int(strArr[0][i]) & int(strArr[1][i]))
    # code goes here
    return s


# keep this function call here
print(BitwiseTwo(["10111", "01101"]))
