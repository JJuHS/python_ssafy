T = int(input())
for tc in range(1, T + 1):
    n, num = map(str, input().split())
    tmp = bin(int(num, 16))
    tmp = tmp[2:]
    ans = '0' * (4 - (len(tmp) % 4) % 4) + tmp
    print(tmp)
    print(f'#{tc} {ans}')
