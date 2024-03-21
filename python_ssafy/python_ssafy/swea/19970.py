T = int(input())

def find_node(arr_, start, end, v_, visited):
    if start == end:
        return 1

    visited[start] = True

    for i in range(1, v_ + 1):
        if arr_[start][i] != 1 or visited[i]:
            continue
        if find_node(arr_, i, end, v_, visited):
            return 1
    return 0


for tc in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [False] * (v + 1)

    for i in range(e):
        tmp = list(map(int, input().split()))
        arr[tmp[0]][tmp[1]] = 1

    s, g = map(int, input().split())

    ans = find_node(arr, s, g, v, visited)
    print(f'#{tc} {ans}')

