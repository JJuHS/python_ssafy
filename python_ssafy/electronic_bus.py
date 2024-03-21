T = int(input())

for tc in range(1, T+1):
    k, n, m = map(int, input().split())     # k 1회이동거리 n 총거리
    bus_list = list(map(int, input().split()))

    cnt = 0
    location = 0
    while location + k < n:
        for i in range(k, 0, -1):

            if i + location in bus_list:
                cnt += 1
                location += i
                break
        else:
            cnt = 0
            break

    if (bus_list[-1] + k) < n:
        cnt = 0


    print(f'#{tc} {cnt}')

