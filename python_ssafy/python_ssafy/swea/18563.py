# 사과먹기게임
from collections import deque as dq
T = int(input())

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def apple(s = (0,0), cnt = 0, idx = 0, goal1 = 1, res = 10**6):
    if s == goal[final]:
        return True
    if s == goal1:
        return apple(s, 0, idx, goal1 + 1, res)
    if cnt == 4:
        return False
    for k in range(1, N):
        nx = s[0] + k * directions[idx][0]
        ny = s[1] + k * directions[idx][1]
        if 0 <= nx < N and 0 <= ny <= N:
            if apple((nx, ny), cnt + 1, idx + 1, goal1, res):
                res = min(res, cnt)
    return res

for tc in range(1, T+1):
    result = 0
    N = int(input())
    farm = []
    goal = {}
    for i in range(N):
        tmp = list(map(int, input().split()))
        farm.append(tmp)
        for j in range(N):
            if tmp[j] != 0:
                goal[tmp[j]] = (i, j)
    final = len(goal)
    z = apple()
    print(f'#{tc} {z}')

