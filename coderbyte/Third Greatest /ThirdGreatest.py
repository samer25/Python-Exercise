def ThirdGreatest(strArr):
    strArr.sort(key=len, reverse=True)

    return strArr[2]


# keep this function call here
print(ThirdGreatest(["hello", "world", "world"]))
