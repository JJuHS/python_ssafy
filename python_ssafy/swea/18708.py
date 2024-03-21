n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: (x[1], x[0]))

end = 0
ans = 0

for s, e in schedule:
    if end <= s:
        ans += 1
        end = e
print(ans)