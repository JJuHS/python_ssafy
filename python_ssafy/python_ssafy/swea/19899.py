a, b = map(int, input().split())
N = 6
Cycle = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

ans = 9999
cnt = 0


def min_node(current, n, current_tmp = [], visited = set(), res = 0):
    global cnt, ans
    visited.update(current)

    if b-1 in visited:
        ans = min(ans, res)
        return

    for cur in current:
        for i in range(n):
            if Cycle[cur][i] == 1:
                current_tmp.append(i)
                if i not in visited:
                    visited.add(i)
                    cnt += 1
                    min_node(list(set(current_tmp)), n, [], visited, res+1)
        if len(current_tmp) == 0:
            continue

min_node([a-1], N)
if ans == 9999:
    ans = 0
print(ans)