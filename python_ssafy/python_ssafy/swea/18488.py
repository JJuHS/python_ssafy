from collections import deque as dq

m, n = map(int, input().split())
k = int(input())

bus_line = []
for _ in range(k):
    tmp = list(map(int, input().split()))
    bus_line.append(tmp[1:])
sx, sy, dx, dy = map(int, input().split())
bus_line += [[sx, sy, sx, sy], [dx, dy, dx, dy]]

def cross(a, b):
    a1, b1, a2, b2, a3, b3, a4, b4 = *bus_line[a], *bus_line[b]
    return max(a1,a2)>=min(a3,a4) and max(a3,a4)>=min(a1,a2) and max(b1,b2)>=min(b3,b4) and max(b3,b4)>=min(b1,b2)

visited = [False] * (k + 2)
q = dq([(-2, -1)])

while q:
    current, cnt = q.popleft()
    if visited[current]:
        continue
    visited[current] = True
    if current == k + 1:
        print(cnt)
        break
    for tmp in range(k + 2):
        if not visited[tmp]:
            if cross(current, tmp):
                q.append((tmp, cnt + 1))
