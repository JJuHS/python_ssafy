T = int(input())
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    ans = 1
    arr = list(map(int, input().split()))
    q = [n]
    for i in range(e):
        if arr[2 * i] in q and arr[2 * i + 1] not in q:
            q.append(arr[2 * i + 1])
            ans += 1
    print(f'#{tc} {ans}')