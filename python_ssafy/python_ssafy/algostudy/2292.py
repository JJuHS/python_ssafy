import sys
n = int(sys.stdin.readline())

s, e, i = 1, 1, 1
while True:
    s = e + 1
    e = 1 + 6 * i
    i += 1
    if s <= n <= e:
        print(i)
        break
