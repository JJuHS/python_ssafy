T = int(input())
for c in range(1, T + 1):
    s = list(set(input()))
    a = list(input())
    b = 0
    for t in s: b = max(b, a.count(t))
    print(f'#{c} {b}')