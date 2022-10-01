def RectangleArea(strArr):
    # code goes here
    x = [int(s.split()[0][1:]) for s in strArr]
    y = [int(s.split()[1][:-1]) for s in strArr]
    return (max(x) - min(x)) * (max(y) - min(y))


# keep this function call here
print(RectangleArea(["(0 0)", "(3 0)", "(0 2)", "(3 2)"]))
