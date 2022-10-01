def NonrepeatingCharacter(strParam):
    for i in strParam:
        if strParam.count(i) == 1:
            return i
    # code goes here


# keep this function call here
print(NonrepeatingCharacter("agettkgaeee"))
