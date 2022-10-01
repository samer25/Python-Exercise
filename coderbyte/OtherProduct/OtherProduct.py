def OtherProducts(arr):
    result = []
    arr_copy = list(arr)
    for i in arr:
        arr_copy.remove(i)
        calc = 1
        for j in arr_copy:
            calc *= j
        result.append(calc)
        arr_copy = list(arr)

    return '-'.join([str(x) for x in result])
# keep this function call here
print(OtherProducts([1, 4, 3]))
