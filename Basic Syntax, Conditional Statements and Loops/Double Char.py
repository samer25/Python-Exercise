# Given a string, you have to print a string in which each character (case-sensitive) is repeated once.

while True:
    text = str(input())
    d_char = ''
    if text == 'End':
        break
    for i in text:
        d_char += i + i

    print(d_char)