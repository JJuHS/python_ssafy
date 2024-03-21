direction1 = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
direction2 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (1, 1)]

def dfs():
    global res
    for i in range(0, n):
        for j in range(0, m):
            if not j % 2:
                tmp = []
                for d in range(6):
                    nx = i + direction1[d][0]
                    ny = j + direction1[d][1]
                    if 0 <= nx < n and 0 <= ny < m:
                        tmp.append(bee[nx][ny])
                if len(tmp) >= 3:
                    tmp.sort(reverse = True)
                    res = max(res, bee[i][j] + sum(tmp[:3]))
            if j % 2:
                tmp = []
                for d in range(6):
                    nx = i + direction2[d][0]
                    ny = j + direction2[d][1]
                    if 0 <= nx < n and 0 <= ny < m:
                        tmp.append(bee[nx][ny])
                if len(tmp) >= 3:
                    tmp.sort(reverse = True)
                    res = max(res, bee[i][j] + sum(tmp[:3]))

def bfs(s, tmp, cnt = 0):
    global res
    if cnt == 3:
        res = max(tmp, res)
        return
    if not s[1] % 2:
        for d in range(6):
            nx = s[0] + direction1[d][0]
            ny = s[1] + direction1[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    bfs((nx, ny), tmp + bee[nx][ny], cnt + 1)
                    visited[nx][ny] = 0
    if s[1] % 2:
        for d in range(6):
            nx = s[0] + direction2[d][0]
            ny = s[1] + direction2[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    bfs((nx, ny), tmp + bee[nx][ny], cnt + 1)
                    visited[nx][ny] = 0

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    dfs()
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            bfs((i, j), bee[i][j])
            visited[i][j] = 0

    print(f'#{tc} {res}')