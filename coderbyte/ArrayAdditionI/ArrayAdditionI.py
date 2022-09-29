from itertools import combinations


def ArrayAdditionI(arr):
    max_num = max(arr)
    arr.remove(max_num)
    list_comb = []
    for i in range(len(arr)):
        list_comb.append(list(combinations(arr, i + 1)))
        list_sum = list(map(sum, list_comb[i]))
        if max_num in list_sum:
            return True
    return False



#
print(ArrayAdditionI([5, 7, 16, 1, 2]))
print(ArrayAdditionI([3, 5, 7, 1, 2, 5, -1, 8, 12]))
print(ArrayAdditionI([3, 5, -1, 8, 12]))
