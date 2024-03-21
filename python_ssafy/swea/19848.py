n = int(input())
ans = 0
for i in range(n):
    s = input()
    a = []
    for x in s:
        if len(a) == 0:
            a.append(x)
            continue
        if a[-1] == x:
            a.pop()
            continue
        if a[-1] != x:
            a.append(x)
    if len(a) == 0:
        ans += 1
print(ans)