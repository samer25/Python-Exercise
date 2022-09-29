def DashInsert(strParam):
    new_str = ''

    for i in range(len(strParam) - 1):
        new_str += strParam[i]
        if int(strParam[i]) % 2 != 0 and int(strParam[i + 1]) % 2 != 0:
            new_str += '-'
    # code goes here
    return new_str + strParam[-1]


# keep this function call here
print(DashInsert('999630'))
