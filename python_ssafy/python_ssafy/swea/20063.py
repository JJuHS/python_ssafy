def dfs(x, y, maze_, end_, N):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if (x, y) == end_:
        return 1

    maze_[x][y] = 1

    for dx, dy in direction:
        tmp_x = x + dx
        tmp_y = y + dy
        if 0 <= tmp_x < N and 0 <= tmp_y < N:
            if maze_[tmp_x][tmp_y] == 0:
                if dfs(tmp_x, tmp_y, maze_, end_, N):
                    return 1
            if maze_[tmp_x][tmp_y] == 3:
                return 1
    return 0

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    maze = []
    start, end = None, None
    for i in range(n):
        tmp = [int(s) for s in input()]
        maze.append(tmp)
        for j in range(n):
            if tmp[j] == 2:
                start = (i,j)
            if tmp[j] == 3:
                end = (i,j)


    ans = dfs(start[0], start[1], maze, end, n)

    print(f'#{tc} {ans}')

#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     maze = []
#     start, end = (0,0), (0,0)
#     for i in range(N):
#         tmp = [int(s) for s in input()]
#         maze.append(tmp)
#
#         for j in range(N):
#             if tmp[j] == 2:
#                 start = (i,j)
#             if tmp[j] == 3:
#                 end = (i,j)
#
#     direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     visited = [[False] * N for _ in range(N)]
#     ans = 0
#
#     def bfs(map_, n, s = (0, 0), e = (1,1)):
#         global ans
#         visited[s[0]][s[1]] = True
#         if visited[e[0]][e[1]]:
#             ans = 1
#             return
#         for i in range(4):
#             tmp_x = s[0] + direction[i][0]
#             tmp_y = s[1] + direction[i][1]
#             if 0 <= tmp_x < n and 0 <= tmp_y < n:
#                 if not visited[tmp_x][tmp_y] and map_[tmp_x][tmp_y] == 0:
#                     bfs(map_, n, (tmp_x, tmp_y))
#         return
#     bfs(maze, N, start, end)
#     print(f'#{tc} {ans}')