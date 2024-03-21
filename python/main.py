import sys
from collections import deque as dq
input = sys.stdin.readline

def bfs(start):
    global res
    q = dq([(start, 0)])
    while q:
        now, time = q.popleft()
        visit_tmp = []
        for next, tmp in road[now]:
            if (now, next) not in visit:
                if next == start and time + tmp < 0:
                    res = 0
                    return
                if next == start:
                    continue
                q.append((next, time + tmp))
                visit_tmp.append((now, next))
        for t1, t2 in visit_tmp:
            visit.append((t1, t2))


T = int(input())
for tc in range(1, T + 1):
    n, m, w = map(int, input().split())
    road = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        road[s].append([e, t])
        road[e].append([s, t])

    for i in range(w):
        S, E, T = map(int, input().split())
        road[S].append([E, -T])
    res = 1
    for i in range(1, n + 1):
        visit = []
        if not res:
            break
        bfs(i)
    print(['YES', 'NO'][res])
