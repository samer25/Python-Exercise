def NumberAddition(strParam):
    num_str = ''
    num = []
    strParam += '*'
    for i in range(len(strParam)):
        if strParam[i].isdigit():
            num_str += strParam[i]
        else:
            if num_str != '':
                num.append(num_str)
            num_str = ''
            # code goes here
    return sum(list(map(int, num)))


# keep this function call here
print(NumberAddition("3Hello 9"))
