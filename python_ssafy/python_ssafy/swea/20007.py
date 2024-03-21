N = int(input())
Map_ = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * N for _ in range(N)]
ans = 0

def bfs(map_, n, start = (0,0)):
    global ans
    visited[start[0]][start[1]] = True
    if visited[n-1][n-1]:
        ans = 1
        return
    for i in range(4):
        tmp_x = start[0] + direction[i][0]
        tmp_y = start[1] + direction[i][1]
        if 0 <= tmp_x < n and 0 <= tmp_y < n:
            if not visited[tmp_x][tmp_y] and map_[tmp_x][tmp_y] == 0:
                bfs(map_, n, (tmp_x, tmp_y))
    return

bfs(Map_, N)
print(ans)