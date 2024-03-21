T = int(input())

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(s, e):
    global cnt
    tmp = []
    if cnt > n * n:
        cnt = 0
        return
    for i in s:
        for j in range(4):
            x_tmp = i[0] + direction[j][0]
            y_tmp = i[1] + direction[j][1]
            if 0 <= x_tmp < n and 0 <= y_tmp < n:
                if maze[x_tmp][y_tmp] == 3:
                    return
                if maze[x_tmp][y_tmp] == 0:
                    if not visited[x_tmp][y_tmp]:
                        visited[x_tmp][y_tmp] = True
                        tmp.append((x_tmp, y_tmp))
    cnt += 1
    bfs(tmp, e)

for tc in range(1, T + 1):
    n = int(input())
    maze = []
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        tmp = input()
        tmp2 = []
        for j in range(n):
            if tmp[j] == '2':
                start = [i, j]
                visited[i][j] = True
            if tmp[j] == '3':
                end = (i, j)
        for k in range(n):
            tmp2.append(int(tmp[k]))
        maze.append(tmp2)
    cnt = 0

    bfs([start], end)

    print(f'#{tc} {cnt}')