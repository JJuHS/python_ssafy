from heapq import heappush, heappop, heapify

Q = int(input())
num = list(map(int, input().split()))

for i in range(Q):
    q = [1]
    heapify(q)
    visit = {1}
    for _ in range(num[i]):
        ugly = heappop(q)
        for pr in [2, 3, 5]:
            ugly_tmp = ugly * pr
            if ugly_tmp not in visit:
                visit.add(ugly_tmp)
                heappush(q, ugly_tmp)

    print(ugly, end = ' ')