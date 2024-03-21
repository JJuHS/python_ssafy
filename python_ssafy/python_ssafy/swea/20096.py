from collections import deque as dq

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    pizza = [[idx+1, value] for idx, value in enumerate(list(map(int, input().split())))]
    q = dq(pizza[:n])
    cnt = n
    visited = [False] * (m + 1)

    while q:
        if len(q) == 1:
            break
        if visited[q[0][0]]:
            if q[0][1] <= 1:
                q.popleft()
                if cnt < m:
                    q.append(pizza[cnt])
                    cnt += 1
                    visited[cnt] = True
                continue
            q[0][1] //=2
        else:
            visited[q[0][0]] = True

        q.append(q.popleft())

    print(f'#{tc} {q[0][0]}')
