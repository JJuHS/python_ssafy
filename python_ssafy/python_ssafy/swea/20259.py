import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    ans = ''
    n = float(input())
    factor = 1
    for i in range(13):
        factor *= 0.5
        if n >= factor:
            n -= factor
            ans += '1'
        else:
            ans += '0'
        if n == 0:
            break
    if len(ans) == 13:
        ans = 'overflow'
    print(f'#{tc} {ans}')
