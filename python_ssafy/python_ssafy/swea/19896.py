N = int(input())
Node = [list(map(int, input().split())) for _ in range(N)]

def visited(n, node, idx = 0, res = []):
    for i in range(n):
        if node[idx][i] == 1:
            res.append(i)
            if len(res) == n:
                return
            visited(n, node, i, res)
    return res

res = visited(N, Node)
print(0, *res)