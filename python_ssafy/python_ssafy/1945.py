def mod(x, y):
    ans = 0
    while x % y == 0:
        ans += 1
        x = x/y
    return ans

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    e = mod(n, 11)
    d = mod(n, 7)
    c = mod(n, 5)
    b = mod(n, 3)
    a = mod(n, 2)
    print(f'#{tc}',a,b,c,d,e)
