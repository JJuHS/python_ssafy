from heapq import heappop, heappush
T = int(input())

def sum_node(N, Arr, ans = 0):
    if N == 0:
        return ans
    tmp = N //2
    return sum_node(tmp, Arr, ans + Arr[tmp])

for tc in range(1, T + 1):
    n = int(input())
    arr = []
    tree = list(map(int, input().split()))
    for i in range(n):
        heappush(arr, tree[i])
    arr = [0] + arr
    res = sum_node(n, arr)
    print(f'#{tc} {res}')

