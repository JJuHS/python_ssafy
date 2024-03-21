import pprint

n = int(input())
q = int(input())

board = [[0] * n for _ in range(n)]
color_arr = []
for _ in range(q):
    color, y1, x1, y2, x2 = map(int, input().split())
    color_arr.append(color)
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] <= color:
                board[i][j] = color
res = 0
for i in range(q):
    visited = [[1] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if board[j][k] == color_arr[i]:
                visited[j][k] += min(visited[j][k - 1], visited[j - 1][k], visited[j - 1][k - 1])
            res = max(res, visited[j][k])
print((res - 1) ** 2)