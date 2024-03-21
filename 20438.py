T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.sort(key = lambda x:x[1])
    ans = []
    ans.append(arr[0])
    for i in range(1, n):
        if ans[-1][1] <= arr[i][0]:
            ans.append(arr[i])

    print(f'#{tc} {len(ans)}')

