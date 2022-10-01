def NextPalindrome(num):
    while True:
        num += 1

        if str(num)[::-1] == str(num):
            return num
    # code goes here
    # return num


# keep this function call here
print(NextPalindrome(24))
