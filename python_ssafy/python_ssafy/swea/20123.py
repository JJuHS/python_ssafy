n, m = map(int, input().split())
bus = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    bus[x][y] = 1
    bus[y][x] = 1
visited = [False] * (n + 1)
t = int(input())
visited[t] = True

start = 1
end = n

cnt = 0
def bfs(s = [1]):
    global cnt
    if cnt > n:
        cnt = -1
        return
    if n in s:
        return
    tmp = []
    for i in s:
        for j in range(1, n + 1):
            if bus[i][j] == 1 and not visited[j]:
                tmp.append(j)
                visited[j] = True
    cnt += 1
    bfs(tmp)
bfs()

print(cnt)

