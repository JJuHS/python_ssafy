T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    box = list(map(int, input().split()))
    box.sort(reverse=True)
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if box[i] and box[i] <= truck[j]:
                truck[j] = 0
                cnt += box[i]
                box[i] = 0
    print(f'#{tc} {cnt}')