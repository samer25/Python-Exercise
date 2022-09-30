def PowersofTwo(num):
    while num % 2 == 0:
        num = num / 2
    if num == 1:
        return True
    return False
    # code goes here


# keep this function call here
print(PowersofTwo(8))
