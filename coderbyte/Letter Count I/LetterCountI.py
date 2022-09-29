def LetterCountI(strParam):
    list_words = strParam.split(' ')
    count_w = 1
    l = {}
    for i in range(len(list_words)):
        word = list_words[i]
        for j in range(len(word)):
            if word.count(word[j]) > count_w:
                l[word] = word.count(word[j])
                count_w += 1
    if l:
        return ''.join(l.keys())
    else:
        return -1
    # code goes here



print(LetterCountI('a b c d ee'))
print(LetterCountI('Hello apple pie'))
