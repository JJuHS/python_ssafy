T = int(input())

def bfs(start, end, n, arr):
    global cnt
    if cnt > n:
        cnt = 0
        return
    if end in start:
        return
    tmp = []
    for i in start:
        for j in range(1, n + 1):
            if arr[i][j] == 1 and not visited[j]:
                tmp.append(j)
                visited[j] = 1
    cnt += 1
    bfs(tmp, end, n, arr)

for tc in range(1, T + 1):
    v, e =  map(int, input().split())
    li = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [False] * (v + 1)
    for _ in range(e):
        x, y =  map(int, input().split())
        li[x][y] = 1
        li[y][x] = 1
    s, g =  map(int, input().split())
    visited[s] = 1
    cnt = 0
    bfs([s], g, v, li)
    print(f'#{tc} {cnt}')