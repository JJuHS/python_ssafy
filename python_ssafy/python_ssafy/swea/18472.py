from collections import deque as dq
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    visited = [False] * 10001
    q = dq()
    q.append([a, ''])
    visited[a] = True

    while q:
        current, command = q.popleft()
        if current == b:
            print(command)
            break
        d = (current * 2) % 10000
        s = (current - 1) % 10000
        l = ((current * 10) + (current // 1000)) % 10000
        r = ((current % 10) * 1000 + (current // 10)) % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, command + 'D'])
        if not visited[s]:
            visited[s] = True
            q.append([s, command + 'S'])
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])

