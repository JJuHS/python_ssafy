def gin(ar):
    cnt = [0] * 10
    for i in ar:
        cnt[i] += 1
    if 3 in cnt:
        return True
    for i in range(7):
        if 0 not in cnt[i:i + 3]:
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    ans = 0
    for i in range(6):
        arr1.append(arr[2 * i])
        arr2.append(arr[2 * i + 1])
        if gin(arr1):
            ans = 1
            break
        if gin(arr2):
            ans = 2
            break

    print(f'#{tc} {ans}')
