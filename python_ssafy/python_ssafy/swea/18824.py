n, q = map(int, input().split())
strong_list = list(map(int, input().split()))
for _ in range(q):
    Si, Ei = map(int, input().split())
    cnt = 0
    for strong in strong_list:
        if Si <= strong <= Ei:
            cnt+=1

    print(cnt)