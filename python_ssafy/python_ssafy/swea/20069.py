def min_sum(arr, n, visited, s = 0, ans = 0):
    global res
    if ans > res:
        return
    if n - 1 == s:
        ans += arr[-1][visited.index(False)]
        res = min(ans, res)
        return
    ar = arr[s]
    for j in range(n):
        if visited[j]:
            continue
        visited[j] = True
        min_sum(arr, n, visited, s + 1, ans + ar[j])
        visited[j] = False
    return

T = int(input())
for tc in range(1, T + 1):
    res = 90
    N = int(input())
    visit = [False] * N
    num_list = [list(map(int, input().split())) for _ in range(N)]
    min_sum(num_list, N, visit)
    print(f'#{tc} {res}')
