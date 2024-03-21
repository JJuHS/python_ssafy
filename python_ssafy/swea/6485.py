T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    bus_list = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    bus_station = [int(input()) for _ in range(p)]
    ans_list = []

    for station in bus_station:
        ans = 0
        for bus in bus_list:
            if bus[0] <= station <= bus[1]:
                ans += 1
        ans_list.append(ans)

    print(f'#{tc}', *ans_list)


