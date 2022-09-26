# Given a Divisor and a Bound, find the largest integer N, such that:
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found

d = int(input())
b = int(input())

while True:
    if b % d == 0:
        if b > 0:
            print(b)
        break
    else:
        b -= 1
