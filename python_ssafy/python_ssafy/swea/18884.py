from heapq import heappush, heappop

n = int(input())
max_q = []
min_q = []
heappush(max_q, -500)

for i in range(1, n + 1):
    tmp1, tmp2 = map(int, input().split())
    for tmp in [tmp1, tmp2]:
        if not max_q or tmp < -max_q[0]:
            heappush(max_q, -tmp)
            if len(max_q) > len(min_q) + 1:
                heappush(min_q, -heappop(max_q))
        else:
            heappush(min_q, tmp)
            if len(max_q) < len(min_q):
                heappush(max_q, -heappop(min_q))
    print(-max_q[0])