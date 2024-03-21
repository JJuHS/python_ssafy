import sys

numbers = list(map(int, sys.stdin.readline().split()))
n = 4 * min(numbers)
while True:
    cnt = 0
    for num in numbers:
        if n % num == 0:
            cnt += 1
    if cnt > 2:
        print(n)
        break
    n += 1
