from collections import deque as dq

def subset(N):
    subset1 = []
    for k in range(1 << N):
        tmp = []
        for j in range(N):
            if k & (1 << j):
                tmp.append(j)
        if len(tmp) <= N//2:
            subset1.append(tmp)
    return subset1

def check(a, b):
    a = list(a)
    b = list(b)
    q = dq([a[0]])
    visited = [0] * n
    while q:
        now = q.popleft()
        visited[now] = 1
        for i in range(n):
            if Rrc[now][i] and not visited[i] and i not in b:
                q.append(i)
    for i in a:
        if not visited[i]:
            return False

    q = dq([b[0]])
    visited = [0] * n
    while q:
        now = q.popleft()
        visited[now] = 1
        for i in range(n):
            if Rrc[now][i] and not visited[i] and i not in a:
                q.append(i)
    for i in b:
        if not visited[i]:
            return False
    return True


def village():
    global ans
    total_arr = set(range(n))
    arr = subset(n)
    visited = []
    for arr_tmp in arr[1:]:
        left = set(arr_tmp)
        if left in visited:
            continue
        right = total_arr - left
        visited.append(right)
        ans_tmp = 0
        if check(left, right):
            for i in left:
                ans_tmp += pi[i]
            for j in right:
                ans_tmp -= pi[j]
            ans = min(abs(ans_tmp), ans)
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    Rrc = []
    for i in range(n):
        tmp_ = list(map(int, input().split()))
        Rrc.append(tmp_)
    pi = list(map(int, input().split()))
    ans = 10 ** 6
    village()
    print(f'#{tc} {ans}')
