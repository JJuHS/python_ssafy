n, m = map(int, input().split())
li = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    li[x][y] = 1
    li[y][x] = 1
s, k = map(int, input().split())

cnt = 0
visited = [False] * (n + 1)
ans = {s}
def bfs(start = [s]):
    global cnt
    if cnt == k:
        return
    tmp = []
    for j in start:
        for i in range(1,n + 1):
            if li[j][i] == 1 and not visited[i]:
                tmp.append(i)
                ans.add(i)
                visited[i] = True
    cnt += 1
    bfs(tmp)

bfs()
print(len(ans))