T = int(input())


def dfs(now = 1, res = 0, cnt = 0):
    global ans
    if cnt == n - 1:
        ans = min(ans, res + arr[now - 1][0])
        return
    for i in range(2, n + 1):
        if not visited[i]:
            visited[i] = True
            dfs(i, res + arr[now - 1][i - 1], cnt + 1)
            visited[i] = False

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * (n + 1)
    ans = 10 ** 6
    dfs()
    print(f'#{tc} {ans}')