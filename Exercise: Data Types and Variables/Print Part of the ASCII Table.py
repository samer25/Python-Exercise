start = int(input())
end = int(input())
result = []
for i in range(start, end + 1):
    result.append(chr(i))

print(' '.join(result))
