T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    ans = 1
    for p in passcode:
        if p in sample:
            a = sample.index(p)
            sample = sample[a:]
        else:
            ans = 0
            break
    print(f'#{tc} {ans}')
