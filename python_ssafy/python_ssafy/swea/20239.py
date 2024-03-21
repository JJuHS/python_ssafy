T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    arr = [0] * (n + 1)
    for i in range(m):
        num, node = map(int, input().split())
        arr[num] = node
    for i in range(n//2, 0, -1):
        try:
            arr[i] = arr[2 * i] + arr[2 * i + 1]
        except:
            arr[i] = arr[2 * i]
    print(f'#{tc} {arr[l]}')
