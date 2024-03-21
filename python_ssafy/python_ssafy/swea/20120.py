n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

visited = [True] + [False] * (n - 1)
ans_li = [0]

def bfs(s = [0]):
    tmp = []
    for j in s:
        for i in range(n):
            if li[j][i] == 1 and not visited[i]:
                visited[i] = True
                tmp.append(i)
                ans_li.append(i)
    if len(tmp) == 0:
        return
    bfs(tmp)
    return

bfs()
print(*ans_li)