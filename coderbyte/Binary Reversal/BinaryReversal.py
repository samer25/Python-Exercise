def BinaryReversal(strParam):
    nums = int(strParam)

    input_bin = '{0:b}'.format(nums)

    while len(input_bin) % 8 != 0:
        input_bin = "0" + input_bin

    rev = input_bin[::-1]

    result = int(rev, 2)
    # code goes here
    return result


# keep this function call here
print(BinaryReversal("47"))
